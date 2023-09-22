// VideoPlayer.js (React frontend)
import React, { useEffect, useState } from 'react';

const VideoPlayer = () => {
  const [videoUrl, setVideoUrl] = useState('');

  useEffect(() => {
    async function fetchVideo() {
      try {
        const response = await fetch('http://localhost:8000/video'); // Assuming your FastAPI server is running on the same host as your React app
        if (response.ok) {
          const blob = await response.blob();
          console.log("Video console");
          const videoUrl = URL.createObjectURL(blob);
          setVideoUrl(videoUrl);
        } else {
          console.error('Failed to fetch video');
        }
      } catch (error) {
        console.error('Error fetching video:', error);
      }
    }

    fetchVideo();
  }, []);

  return (
    <div>
      {videoUrl && (
        <video controls width="640" height="360">
          <source src={videoUrl} type="video/mp4" />
          Your browser does not support the video tag.
        </video>
      )}
    </div>
  );
};

export default VideoPlayer;
