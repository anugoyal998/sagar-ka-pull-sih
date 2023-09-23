import React from "react";
import VideoPlayer from "./components/VideoPlayer";
import Navbar from "./components/Navbar";
import About from "./components/About";
import ScrollToTop from "./components/ScrollToTop";

const App = () => {
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
