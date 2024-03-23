import "./App.css";

import { useEffect, useState } from "react";

function App() {
  const [data, setdata] = useState([]);

  useEffect(() => {
    const requestData = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
    };

    fetch("http://localhost:8000/api/all-data", requestData)
      .then((respons) => respons.json())
      .then((data) => {
        setdata(data);
        console.log(data);
      })
      .catch((e) => {
        console.log(e);
      });
  }, []);

  return (
    <div className="App">
      <ul>
        {data.map((item) => (
          <li key={item.id}>
            <p>ID: {item.id}</p>
            <p>SID: {item.sid}</p>
            <p>Name: {item.name}</p>
            <p>Age: {item.age}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
