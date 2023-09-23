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
      <div className="flex flex-row">
        <div className="basis-3/4">
          <img
            className="video_player"
            src="http://localhost:8000/stream_video"
          />
        </div>
        <div className="basis-1/4">
          <div class="table_panel w-full max-w-md p-4 rounded-lg shadow sm:p-8 bg-gray-800 border-gray-700">
            <div class="flex items-center justify-between mb-4">
              <h5 class="text-xl font-bold leading-none">Video Data</h5>
            </div>
            <div class="flow-root">
              <ul role="list" class="divide-y divide-gray-700">
                <li class="py-3 sm:py-4">
                  <div class="flex items-center space-x-4">
                    <div class="flex-shrink-0"></div>
                    <div class="flex-1 min-w-0">
                      <p class="text-sm font-medium truncate ">Crowd Count</p>
                    </div>
                    <div class="inline-flex items-center text-base font-semibold ">
                      320
                    </div>
                  </div>
                </li>
                <li class="py-3 sm:py-4">
                  <div class="flex items-center space-x-4">
                    <div class="flex-shrink-0"></div>
                    <div class="flex-1 min-w-0">
                      <p class="text-sm font-medium truncate ">Fire</p>
                    </div>
                    <div class="inline-flex items-center text-base font-semibold">
                      False
                    </div>
                  </div>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default VideoPlayer;
