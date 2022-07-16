import { useState } from 'react'
import '../App.css'

function Form() {
    const [position, setPosition] = useState(0)
    const [sum, setSum] = useState(0)
    const [list, setList] = useState([])
    const [pairs, setPairs] = useState(null)

    function handleAdd() {
        setList(list.concat(position))
    }

    function handleReset() {
        setList([])
    }

    async function findPairs() {
        const strList = list.join(',')
        const url = `//localhost:8080/sum/${strList}/${sum}`
        console.log(url)
        const api = await fetch(url)
        const data = await api.json()
        console.info(data)
        setPairs(JSON.stringify(data?.pairs))
    }

    return (
      <div className="card">
        <label htmlFor="integers">Input integers: </label>
        <br/>
        <input type="number" id="integers" name="integers" value={position}
            onChange={(e) => setPosition(e.target.value)} />
        <br/>
        <button onClick={handleAdd}>
          Add integer {position}
        </button>
        <button onClick={handleReset}>
          Reset list
        </button>
        <p>
          [<code>{list?.join(',')}</code>]
        </p>
        <label htmlFor="sum">Sum expected: </label>
        <br/>
        <input type="number" id="sum" name="sum" value={sum}
            onChange={(e) => setSum(e.target.value)} />
        <br/>
        <button onClick={findPairs} disabled={list.length < 2}>
          Find Pairs
        </button>
        <p>
          <code>{pairs}</code>
        </p>
      </div>
    )
}

export default Form
