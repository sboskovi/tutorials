import { useState } from 'react'
import './App.css'

import type { Todo as ITodo } from "./interfaces/Todo";

import Todos from "./components/Todo";


const initialTodos: Array<ITodo> = [
  {
    id: 0,
    title: "Prepare for the react interview",
    completed: false
  },
  {
    id: 1,
    title: "Prepare for the LeetCode interview",
    completed: false
  },
  {
    id: 2,
    title: "Prepare for the Systems Design interview",
    completed: false
  },
]

function App() {
  const [count, setCount] = useState<number>(0);
  const [todos, setTodos] = useState<Array<ITodo>>(initialTodos);

  function handleCountInc() {
    setCount(count => count + 1);
    setTodos(todos => {
      const id: number = todos.length;
      return [
        ...todos,
        {
          id,
          title: `Btn todo ${id}`,
          completed: false,
        }
      ];
    })
  }

  function handleCompleted(todoId: number): void {
    setTodos((todos) => {
      const new_todos = [...todos];
      const todo = new_todos.find(todo => todo.id === todoId);
      if (todo) {
        todo.completed = true
      }
      return new_todos
    })
  }

  return (
    <>
      <div>
        <button onClick={handleCountInc}>Click me ({count})</button>
      </div>
      <div>
        <Todos todos={todos} onMarkCompleted={handleCompleted} />
      </div>
    </>
  )
}

export default App
