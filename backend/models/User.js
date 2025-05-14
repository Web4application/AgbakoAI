const db = require('../config/db');
const bcrypt = require('bcryptjs');

class User {
  static create(username, password, callback) {
    const hashedPassword = bcrypt.hashSync(password, 10);
    db.query(
      'INSERT INTO users (username, password) VALUES (?, ?)',
      [username, hashedPassword],
      callback
    );
  }

  static findByUsername(username, callback) {
    db.query('SELECT * FROM users WHERE username = ?', [username], callback);
  }
}

module.exports = User;
