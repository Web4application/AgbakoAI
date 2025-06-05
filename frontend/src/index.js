import React from 'react';
import ReactDOM from 'react-dom/client';
import ErrorBoundary from './ErrorBoundary';
import AgbakoAIApp from './AgbakoAIApp';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <ErrorBoundary>
    <AgbakoAIApp />
  </ErrorBoundary>
);
