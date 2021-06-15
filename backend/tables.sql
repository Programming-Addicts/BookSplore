CREATE TABLE users(
first_name VARCHAR(100),
last_name VARCHAR(100),
email VARCHAR(255) NOT NULL UNIQUE,
avatar_url text);