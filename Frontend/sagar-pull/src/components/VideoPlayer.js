import React from "react";
import "../assets/VideoPlayer.css";

import React, { useEffect, useState } from "react";

const VideoPlayer = () => {
  const [videoUrl, setVideoUrl] = useState("");

  useEffect(() => {
    // Fetch the video URL from the backend
    fetch("/api/video") // Replace with your actual backend endpoint
      .then((response) => response.json())
      .then((data) => {
        setVideoUrl(data.videoUrl); // Assuming your backend returns a URL
      })
      .catch((error) => {
        console.error("Error fetching video:", error);
      });
  }, []);

  return (
    <div>
      <video controls width="640" height="360">
        <source src={videoUrl} type="video/mp4" />
        Your browser does not support the video tag.
      </video>
    </div>
  );
};

export default VideoPlayer;
