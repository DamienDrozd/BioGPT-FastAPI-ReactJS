import { useState } from "react";
import './App.css';

function App() {
  const [note, setNote] = useState("")
  const [result, setResult] = useState("")
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState("")


  const handleChange = (e) => {
    setNote(e.target.value)
  }

  const replaceNote = () => {
    setError("")
    setLoading(true)
    fetch("http://127.0.0.1:8000/note?new_note=" + note, { method: "POST", mode: "cors" }).then(res => {
      res.json().then(response => {
        setLoading(false)
        console.log(response)
        setResult(response.suggest)
      })
    }).catch(err => {
      setLoading(false)
      console.log(err)
      setError(err.message)
    })
  }



  return (
    <div className="App">
      <header className="App-header">
        <input className="TextInput" type="text" value={note} onChange={handleChange} />
        <button className="Button" onClick={replaceNote} >Send note</button>
        <div className="resultDiv">
          <p>result : {result}</p>
        </div>
        {loading &&
          <p>Loading</p>
        }
        {error &&
          <p>error : {error}</p>
        }
      </header>
    </div>
  );
}

export default App;
