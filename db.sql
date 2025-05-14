CREATE DATABASE web4cpanel;

USE web4cpanel;

CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(100) NOT NULL,
  password VARCHAR(100) NOT NULL
);

INSERT INTO users (username, password) VALUES ('admin', 'hashed_password_here');
