import {useState} from 'react';

export default function Project({ project }) {
  const [newTask, setNewTask] = useState();

  if (project === null) {
    return <></>;
  }
  const [tasks, setTasks] = useState(project.tasks);

  function addNewTask() {
    if (!project.tasks) {
      project.tasks = []
    }

    project.tasks = [newTask, ...project.tasks];
    setNewTask("");
  }


  function clearTask(task) {
    setTasks((_tasks) => {
      let newTasks = [];
      if (!_tasks) {
        newTasks = [...project.tasks];
      } else {
        newTasks = [..._tasks] 
      }
      newTasks.filter((_task) => _task != task)
      project.tasks = newTasks;
      return newTasks;
    })
  }

  return (
    <span className="project">
      <h1>{project.title}</h1>
      <h3>{project.dueDate}</h3>
      <p>{project.description}</p>
      <hr />
      <h1>Tasks</h1>
      <input onChange={(e) => setNewTask(e.target.value)} />
      <button onClick={addNewTask}>Add Task</button>
      {tasks &&
      <ul>
        {tasks.map((task, index) => <li key={index}>
          {task}
          <button onClick={() => clearTask(task)}>Clear</button>
          </li>)}
      </ul>}
    </span>
  );
}
