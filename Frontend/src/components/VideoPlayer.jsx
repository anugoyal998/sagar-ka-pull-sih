// VideoPlayer.js (React frontend)
import React, { useEffect, useState } from "react";
import "../assets/css/VideoPlayer.css";
import vid from "../assets/result_compressed.mp4";

const VideoPlayer = () => {
  //   const [videoUrl, setVideoUrl] = useState("");

  //   useEffect(() => {
  //     async function fetchVideo() {
  //       try {
  //         const response = await fetch("http://localhost:53090/video"); // Assuming your FastAPI server is running on the same host as your React app
  //         if (response.ok) {
  //           const blob = await response.blob();
  //           console.log("Video console");
  //           const videoUrl = URL.createObjectURL(blob);
  //           setVideoUrl(videoUrl);
  //         } else {
  //           console.error("Failed to fetch video");
  //         }
  //       } catch (error) {
  //         console.error("Error fetching video:", error);
  //       }
  //     }

  //     fetchVideo();
  //   }, []);

  return (
    <div className="video_bg">
      <video className="video_player" controls>
        <source src={vid} type="video/mp4" />
        Your browser does not support the video tag.
      </video>
    </div>
  );
};

export default VideoPlayer;
