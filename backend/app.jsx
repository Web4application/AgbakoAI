import React, { useState } from "react";
import { login, getTreatment } from "./api";

export default function App() {
  const [token, setToken] = useState(null);
  const [symptom, setSymptom] = useState("");
  const [treatment, setTreatment] = useState("");
  const [progress, setProgress] = useState(0);

  const handleLogin = async (e) => {
    e.preventDefault();
    const form = e.target;
    const username = form.username.value;
    const password = form.password.value;
    const token = await login(username, password);
    setToken(token);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setTreatment("");
    setProgress(0);

    const ws = new WebSocket("ws://localhost:8000/ws/progress");
    ws.onmessage = (event) => {
      const progressNum = parseInt(event.data.replace("Progress: ", "").replace("%", ""));
      setProgress(progressNum);
      if (progressNum === 100) ws.close();
    };

    const result = await getTreatment(symptom, token);
    setTreatment(result.treatment);
  };

  if (!token) {
    return (
      <form onSubmit={handleLogin}>
        <input name="username" placeholder="Username" required />
        <input name="password" placeholder="Password" type="password" required />
        <button type="submit">Login</button>
      </form>
    );
  }

  return (
    <>
      <form onSubmit={handleSubmit}>
        <input
          placeholder="Enter symptom"
          value={symptom}
          onChange={(e) => setSymptom(e.target.value)}
          required
        />
        <button type="submit">Get Treatment</button>
      </form>
      <div>Progress: {progress}%</div>
      {treatment && <div><strong>Treatment:</strong> {treatment}</div>}
    </>
  );
}
