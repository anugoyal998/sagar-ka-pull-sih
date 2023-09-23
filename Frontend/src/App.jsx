import React, { useEffect } from 'react'
const App = () => {

  // useEffect(() => {
  //   const ws = new WebSocket('ws://localhost:8000/video')
  //   ws.onopen = (event) => {
  //     ws.send('connect')
  //   }

  //   ws.onmessage = (ev) => {
  //     console.log(ev)
  //     const recv = JSON.parse(ev.data)
  //     console.log(recv)
  //   }

  //   return () => {
  //     ws.close()
  //   }
  // },[])

  return (
    <div>
      <p>anubhav</p>
      <img src="http://localhost:8000/stream_video" />
    </div>
  )
}

export default App