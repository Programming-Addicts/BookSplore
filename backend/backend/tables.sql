CREATE TABLE users(
id BIGSERIAL PRIMARY KEY,
session_id text UNIQUE,
first_name VARCHAR(100),
last_name VARCHAR(100),
email VARCHAR(255) NOT NULL UNIQUE,
avatar_url text,
followers json DEFAULT '[]',
following json DEFAULT '[]'
);