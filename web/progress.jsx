import React, { useState, useEffect } from 'react';

const Progress = () => {
  const [progress, setProgress] = useState('');

  useEffect(() => {
    const ws = new WebSocket('ws://localhost:8000/ws/progress');

    ws.onmessage = (event) => {
      setProgress(event.data);
    };

    ws.onclose = () => console.log("WebSocket closed");

    return () => ws.close();
  }, []);

  return <div style={{ whiteSpace: 'pre-wrap', marginTop: '1rem' }}>{progress}</div>;
};

export default Progress;
