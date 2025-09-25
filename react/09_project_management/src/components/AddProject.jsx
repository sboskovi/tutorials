import { useState } from "react";

export default function AddProject({ onCancelProject, onSaveProject }) {
  const [title, setTitle] = useState();
  const [description, setDescription] = useState();
  const [dueDate, setDueDate] = useState();

  function handleSave() {
    console.log(dueDate);
    onSaveProject({
      title: title,
      description: description,
    });
  }

  return (
    <section className="add-project">
      <button className="cancel-button" onClick={onCancelProject}>
        Cancel
      </button>
      <button className="save-button" onClick={handleSave}>
        Save
      </button>
      <h3>Title</h3>
      <input onChange={(e) => setTitle(e.target.value)} />
      <h3>Description</h3>
      <input onChange={(e) => setDescription(e.target.value)} />
      <h3>Due date</h3>
      <input type="date" onChange={(e) => setDueDate(e.target.value)} />
    </section>
  );
}
