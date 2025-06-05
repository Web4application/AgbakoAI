import React, { useState, useEffect } from 'react';

const AgbakoAIApp = () => {
  const [apiBaseUrl, setApiBaseUrl] = useState('http://localhost:8000');
  const [industry, setIndustry] = useState('healthcare');
  const [task, setTask] = useState('');
  const [data, setData] = useState('');
  const [result, setResult] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const runTask = async () => {
    setLoading(true);
    setError(null);
    setResult('');
    try {
      const res = await fetch(
        `${apiBaseUrl}/ai/run-task?industry=${industry}&task=${task}`,
        {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            Authorization: 'Bearer supersecrettoken',
          },
          body: JSON.stringify({ data: JSON.parse(data || '{}') }),
        }
      );

      if (!res.ok) {
        const err = await res.json();
        throw new Error(err.detail || 'Unknown API error');
      }

      const json = await res.json();
      setResult(JSON.stringify(json.result, null, 2));
    } catch (e) {
      setError(e.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: 20, fontFamily: 'Arial' }}>
      <h1>AgbakoAI Task Runner</h1>

      <label>
        API Base URL:
        <input
          value={apiBaseUrl}
          onChange={e => setApiBaseUrl(e.target.value)}
          style={{ width: '100%', marginBottom: 10 }}
        />
      </label>

      <label>
        Industry:
        <select
          value={industry}
          onChange={e => setIndustry(e.target.value)}
          style={{ width: '100%', marginBottom: 10 }}
        >
          <option value="healthcare">Healthcare</option>
          <option value="finance">Finance</option>
        </select>
      </label>

      <label>
        Task:
        <input
          type="text"
          value={task}
          onChange={e => setTask(e.target.value)}
          placeholder="e.g. diagnose"
          style={{ width: '100%', marginBottom: 10 }}
        />
      </label>

      <label>
        Data (JSON format):
        <textarea
          value={data}
          onChange={e => setData(e.target.value)}
          placeholder='{"symptom": "fever"}'
          rows={6}
          style={{ width: '100%', marginBottom: 10 }}
        />
      </label>

      <button onClick={runTask} disabled={loading}>
        {loading ? 'Running...' : 'Run Task'}
      </button>

      {error && <p style={{ color: 'red' }}>Error: {error}</p>}
      {result && (
        <pre
          style={{
            backgroundColor: '#eee',
            padding: 10,
            marginTop: 20,
            whiteSpace: 'pre-wrap',
            wordWrap: 'break-word',
          }}
        >
          {result}
        </pre>
      )}
    </div>
  );
};

export default AgbakoAIApp;
