import React, { useState, useEffect } from 'react';

const AgbakoAIApp = () => {
  const [apiBaseUrl, setApiBaseUrl] = useState('/api'); // default API base path
  const [industry, setIndustry] = useState('healthcare');
  const [task, setTask] = useState('');
  const [data, setData] = useState('');
  const [result, setResult] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Load from env if available (e.g., REACT_APP_API_BASE_URL)
    const envApi = process.env.vite-react-two-steel.vercel.app;
    if (envApi) setApiBaseUrl(envApi);
  }, []);

  const runTask = async () => {
    setLoading(true);
    setError(null);
    setResult('');
    try {
      const res = await fetch(`${apiBaseUrl}/ai/run-task?industry=${industry}&task=${task}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ data }),
      });

      if (!res.ok) {
        const err = await res.json();
        throw new Error(err.detail || 'Unknown API error');
      }

      const json = await res.json();
      setResult(JSON.stringify(json, null, 2));
    } catch (e) {
      setError(e.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: 600, margin: '2rem auto', fontFamily: 'Segoe UI, sans-serif' }}>
      <h1>⚡ AgbakoAI Frontend</h1>

      <label style={{ display: 'block', marginBottom: 10 }}>
        API Base URL:
        <input
          value={apiBaseUrl}
          onChange={e => setApiBaseUrl(e.target.value)}
          placeholder="https://yourapi.com"
          style={{ width: '100%', padding: 8, marginTop: 4 }}
        />
      </label>

      <label style={{ display: 'block', marginBottom: 10 }}>
        Industry:
        <select
          value={industry}
          onChange={e => setIndustry(e.target.value)}
          style={{ width: '100%', padding: 8, marginTop: 4 }}
        >
          <option value="healthcare">Healthcare</option>
          <option value="finance">Finance</option>
          <option value="education">Education</option>
          <option value="marketing">Marketing</option>
          {/* Add more industries here */}
        </select>
      </label>

      <label style={{ display: 'block', marginBottom: 10 }}>
        Task:
        <input
          type="text"
          value={task}
          onChange={e => setTask(e.target.value)}
          placeholder="e.g., predict_disease"
          style={{ width: '100%', padding: 8, marginTop: 4 }}
        />
      </label>

      <label style={{ display: 'block', marginBottom: 10 }}>
        Input Data (JSON):
        <textarea
          value={data}
          onChange={e => setData(e.target.value)}
          rows={6}
          placeholder='{"symptom": "fever", "age": 30}'
          style={{ width: '100%', padding: 8, marginTop: 4, fontFamily: 'monospace' }}
        />
      </label>

      <button
        onClick={runTask}
        disabled={loading}
        style={{
          padding: '0.75rem 1.5rem',
          fontSize: 16,
          backgroundColor: '#007acc',
          color: 'white',
          border: 'none',
          cursor: loading ? 'not-allowed' : 'pointer',
          marginTop: 10,
          width: '100%',
        }}
      >
        {loading ? 'Running...' : 'Run Task'}
      </button>

      {error && (
        <div style={{ marginTop: 20, color: 'red', whiteSpace: 'pre-wrap' }}>
          Error: {error}
        </div>
      )}

      {result && (
        <pre
          style={{
            marginTop: 20,
            backgroundColor: '#f0f0f0',
            padding: 15,
            borderRadius: 4,
            whiteSpace: 'pre-wrap',
            maxHeight: 400,
            overflowY: 'auto',
          }}
        >
          {result}
        </pre>
      )}
    </div>
  );
};

export default AgbakoAIApp;
