import React, { useState } from "react";

const API_BASE = "http://127.0.0.1:8000";

export default function AgbakoAI() {
  const [username, setUsername] = useState("admin");
  const [password, setPassword] = useState("secret");
  const [token, setToken] = useState("");
  const [industry, setIndustry] = useState("healthcare");
  const [task, setTask] = useState("diagnosis");
  const [inputData, setInputData] = useState('{"symptoms": ["fever"]}');
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  async function login() {
    setError(null);
    try {
      const res = await fetch(`${API_BASE}/token`, {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: new URLSearchParams({ username, password }),
      });
      if (!res.ok) {
        throw new Error("Login failed");
      }
      const data = await res.json();
      setToken(data.access_token);
      setResult(null);
    } catch (e) {
      setError(e.message);
    }
  }

  async function runTask() {
    setError(null);
    setResult(null);
    if (!token) {
      setError("You must login first");
      return;
    }
    let parsedData;
    try {
      parsedData = JSON.parse(inputData);
    } catch {
      setError("Input data must be valid JSON");
      return;
    }

    try {
      const res = await fetch(
        `${API_BASE}/ai/run-task?industry=${industry}&task=${task}`,
        {
          method: "POST",
          headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ data: parsedData }),
        }
      );
      if (!res.ok) {
        const errJson = await res.json();
        throw new Error(errJson.detail || "Task failed");
      }
      const json = await res.json();
      setResult(json.result);
    } catch (e) {
      setError(e.message);
    }
  }

  return (
    <div style={{ fontFamily: "monospace", padding: 20, maxWidth: 600 }}>
      <h2>AgbakoAI Login</h2>
      <input
        placeholder="Username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        style={{ width: "100%", marginBottom: 8 }}
      />
      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        style={{ width: "100%", marginBottom: 8 }}
      />
      <button onClick={login} disabled={!!token}>
        {token ? "Logged In" : "Login"}
      </button>

      <hr style={{ margin: "20px 0" }} />

      <h2>Run AI Task</h2>
      <label>
        Industry:{" "}
        <select
          value={industry}
          onChange={(e) => setIndustry(e.target.value)}
          style={{ marginBottom: 12 }}
        >
          <option value="healthcare">Healthcare</option>
          <option value="finance">Finance</option>
          <option value="education">Education</option>
          <option value="marketing">Marketing</option>
        </select>
      </label>

      <label>
        Task:{" "}
        <input
          value={task}
          onChange={(e) => setTask(e.target.value)}
          style={{ width: "100%", marginBottom: 12 }}
        />
      </label>

      <label>
        Input Data (JSON):{" "}
        <textarea
          rows={6}
          value={inputData}
          onChange={(e) => setInputData(e.target.value)}
          style={{ width: "100%", marginBottom: 12, fontFamily: "monospace" }}
        />
      </label>

      <button onClick={runTask} disabled={!token}>
        Run Task
      </button>

      {error && (
        <pre style={{ color: "red", marginTop: 16 }}>
          Error: {error}
        </pre>
      )}

      {result && (
        <pre
          style={{
            marginTop: 16,
            padding: 12,
            background: "#f0f0f0",
            borderRadius: 6,
          }}
        >
          Result: {typeof result === "object" ? JSON.stringify(result, null, 2) : result}
        </pre>
      )}
    </div>
  );
}
