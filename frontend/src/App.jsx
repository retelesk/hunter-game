import { useState, useEffect } from "react";

function App() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    // Gọi thử API từ Backend
    fetch("http://localhost:8000/")
      .then((res) => res.json())
      .then((data) => setMessage(data.message))
      .catch((err) => console.error("Lỗi kết nối:", err));
  }, []);

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h1>React + FastAPI AR Game</h1>
      <h2>Backend says: {message || "Đang kết nối..."}</h2>
    </div>
  );
}

export default App;
