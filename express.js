const express = require('express');
const app = express();
const port = 3000;

app.get('/api/domains', (req, res) => {
  res.send('List of Domains');
});

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
