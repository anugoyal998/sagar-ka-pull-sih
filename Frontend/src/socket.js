import { io } from "socket.io-client";

export const initSocket = async () => {
    const options = {
      "force new connection": true,
      reconnectionAttempt: "Infinity",
      timeout: 10000,
      transports: ["websocket"],
    };
    const socket = io(
      `ws://localhost:8000/ws`,
      options
    );
    return socket;
  };