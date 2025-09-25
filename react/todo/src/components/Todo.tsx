import type { Todo as ITodo } from "../interfaces/Todo";
import "./todos.css"


interface ITodos {
  todos: Array<ITodo>;
  onMarkCompleted: (id: number) => void;
}

export default function Todos({ todos, onMarkCompleted }: ITodos) {
  return (
    <ul>
      {
        todos.map((todo: ITodo) => 
          <li key={todo.id}>
            <span>
              {todo.title} 
            </span>
            <button disabled={todo.completed} onClick={() => onMarkCompleted(todo.id)}>
              {todo.completed ? "Done" : "Mark completed"}
            </button>
          </li>
        )
      }
    </ul>
  )
}