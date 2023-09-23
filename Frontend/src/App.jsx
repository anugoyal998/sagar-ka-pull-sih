
import React from "react";
import VideoPlayer from "./components/VideoPlayer";
import Navbar from "./components/Navbar";
import About from "./components/About";
import ScrollToTop from "./components/ScrollToTop";



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

      <Navbar></Navbar>
      <ScrollToTop></ScrollToTop>
      <VideoPlayer></VideoPlayer>
      <About></About>




    </div>
  );
};

export default App;
