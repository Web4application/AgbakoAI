const User = require('../models/User');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');

exports.login = (req, res) => {
  const { username, password } = req.body;

  User.findByUsername(username, (err, results) => {
    if (err) return res.status(500).send('Database error');
    if (results.length === 0) return res.status(400).send('Invalid username or password');

    const user = results[0];
    const isMatch = bcrypt.compareSync(password, user.password);
    if (!isMatch) return res.status(400).send('Invalid username or password');

    const token = jwt.sign({ userId: user.id }, process.env.JWT_SECRET, { expiresIn: '1h' });
    res.json({ token });
  });
};
