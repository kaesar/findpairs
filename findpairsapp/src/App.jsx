import { useState } from 'react'
import reactLogo from './assets/react.svg'
import './App.css'
import Form from './features/Form'

function App() {
  return (
    <div className="App">
      <div>
        <a href="https://reactjs.org" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Find Pairs</h1>
      <Form />
    </div>
  )
}

export default App
