import React, { useEffect } from 'react'
import './App.css'

// ==================================== NOTES ==================================== 
// Would you use TS?
// Would you use REDUX?

// Util functions, consider them black box
// Pass anything that will make a valid date
const formatTime = (date) => {
  date = new Date(date);
  var hours = date.getHours();
  var minutes = date.getMinutes();
  var ampm = hours >= 12 ? "pm" : "am";
  hours = hours % 12;
  hours = hours ? hours : 12; // the hour '0' should be '12'
  minutes = minutes < 10 ? "0" + minutes : minutes;
  var strTime = hours + ":" + minutes + " " + ampm;
  return strTime;
};

// Compare two items such that the return value follows this rule:
// If compareFunction(a, b) returns a value > than 0, sort b before a.
// If compareFunction(a, b) returns a value ≤ 0, leave a and b in the same order.
const compareFunction = (first, second) => {
  if (!first && !second) {
    return 0;
  }
  if (first.isCompleted && !second.isCompleted) {
    return 1;
  }
  if (!first.isCompleted && second.isCompleted) {
    return -1;
  }

  return first.starts - second.starts;
};

// NOTE: destructured props? Name collision? ({item, complete, remove})
const Item = (props) => {
  const complete = () => {
    // NOTE: had hard time remembering to call props.complete function
    props.complete(props.item)
  };

  const remove = () => {
    props.remove(props.item)
  };

  // NOTE: why is `props.item && ...` not preferred way to go - ternary operator
  return (
    <li>
      <span className={props.item.isCompleted && 'strikethrough'}>
      {props.item && `${props.item.title} // ${formatTime(props.item.starts)}`}
      </span>
      {!props.item.isCompleted &&<button onClick={complete}>Complete</button>}
      {props.item.isCompleted && <button onClick={remove}>Remove</button>}
    </li>
  );
};

const titles = {
  no_items: "There appear to be no items on your TODO list!",
  no_done: "Let's have a productive day!",
  some_done: "Rock on!",
  all_done: "Congratulations!",
};

const TodoApp = (props) => {
  // NOTE: also problematic, you wanted to add second state with isCompleted bools
  let [items, setItems] = React.useState(props.items.map((item) => ({
    ...item,
    isCompleted: false,
  })));
  let [title, setTitle] = React.useState(titles['no_items']);

  const complete = (item) => {
    // NOTE:you tired with setItems([..items, {...item, isCompleted: true}])
    setItems(items.map((elem) => {
      if (elem.id == item.id) {
        return {...elem, isCompleted: true};
      }
      return elem;
    }))
  };
  
  const remove = (item) => {
    setItems(items.filter((elem) => elem.id != item.id))
  };

  React.useEffect(() => {
    // NOTE: Write and use getTitle() function instead of useEffect() 
    // NOTE: WTF did you say I would not return setTitle here??????
    // NOTE: you got stuck trying to solve how this title should be set inside this useEffect
    // NOTE: === instead of ==
    if (items.length == 0) {
      return setTitle(titles['no_items'])
    }
    // NOTE: filter had hard time filter function
    let completedItemCount = items.filter((item) => item.isCompleted).length;
    if (completedItemCount == items.length) {
      return setTitle(titles['all_done'])
    }
    if (completedItemCount != items.length && completedItemCount > 0) {
      return setTitle(titles['some_done'])
    }
    if (completedItemCount == 0) {
      return setTitle(titles['no_done'])
    }
  }, [items])

  // NOTE: You had hard time remembering how to pass prop to child component
  return (
    <div>
      <p className="title">{title}</p>
      <ul>
        {items && items.sort(compareFunction).map((item) => <Item item={item} complete={complete} remove={remove} />)}
      </ul>
    </div>
  );
};

function App() {
  return (
    <div className="app">
      <TodoApp
        items={[
          { id: 1, title: "Wake up", starts: 1625807718000 },
          { id: 2, title: "Training", starts: 1625809518000 },
          { id: 3, title: "Meeting with Aaron", starts: 1625823318000 },
          { id: 4, title: "Dentist's appointment", starts: 1625814918000 },
          { id: 5, title: "Breakfast", starts: 1625814018000 },
        ]}
      />
    </div>
  )
}

export default App
