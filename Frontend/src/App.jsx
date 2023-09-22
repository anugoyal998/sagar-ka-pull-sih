import React from "react";
import VideoPlayer from "./components/VideoPlayer";
import Navbar from "./components/Navbar";
import About from "./components/About";
import TableData from "./components/TableData";
import ScrollToTop from "./components/ScrollToTop";

const App = () => {
  return (
    <div>
      <Navbar></Navbar>
      <ScrollToTop></ScrollToTop>
      <VideoPlayer></VideoPlayer>
      <TableData></TableData>
      <About></About>
    </div>
  );
};

export default App;
