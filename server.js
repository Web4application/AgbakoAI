const express = require('express');
const mysql = require('mysql2');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcryptjs');
const app = express();

app.use(express.json());

// Setup database connection
const db = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'yourpassword',
  database: 'web4cpanel'
});

// Simple route
app.get('/api', (req, res) => {
  res.send('Web4 cPanel API');
});

// User login route
app.post('/login', async (req, res) => {
  const { username, password } = req.body;
  // Find user by username
  db.query('SELECT * FROM users WHERE username = ?', [username], async (err, results) => {
    if (err) return res.status(500).send('Server error');
    if (results.length === 0) return res.status(400).send('Invalid username or password');

    const user = results[0];
    const isMatch = await bcrypt.compare(password, user.password);
    if (!isMatch) return res.status(400).send('Invalid username or password');

    // Generate token
    const token = jwt.sign({ userId: user.id }, 'your_jwt_secret', { expiresIn: '1h' });
    res.json({ token });
  });
});

// Start the server
app.listen(5000, () => {
  console.log('Server running on port 5000');
});
