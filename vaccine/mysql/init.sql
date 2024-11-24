CREATE DATABASE if not exists test;

USE test;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255),
    password VARCHAR(255)
);

INSERT INTO users (id, username, password) VALUES
(1, 'admin', 'admin123'),
(2, 'user1', 'password1'),
(3, 'user2', 'password2');

CREATE TABLE posts (
	id INT AUTO_INCREMENT PRIMARY KEY,
	title VARCHAR(255),
	content TEXT,
	user_id INT,
	FOREIGN KEY (user_id) REFERENCES users(id)
);

INSERT INTO posts (id, title, content, user_id) VALUES
(1, 'Post 1', 'Content of post 1', 1),
(2, 'Post 2', 'Content of post 2', 2),
(3, 'Post 3', 'Content of post 3', 3);
