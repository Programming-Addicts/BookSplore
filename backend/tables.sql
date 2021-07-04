CREATE TABLE users(
id BIGSERIAL PRIMARY KEY,
first_name VARCHAR(100),
last_name VARCHAR(100),
discriminator INTEGER CONSTRAINT integer_range CHECK (discriminator >= 1000 AND discriminator <= 9999),
username VARCHAR(500),
email VARCHAR(255) NOT NULL UNIQUE,
avatar_url TEXT,
followers json DEFAULT '[]',
following json DEFAULT '[]',
recent_books json DEFAULT '[]'
);

ALTER TABLE users
    ADD CONSTRAINT unique_username UNIQUE(first_name, last_name, discriminator, username);

CREATE TABLE reviews(
    id BIGSERIAL PRIMARY KEY,
    book_id VARCHAR(150) NOT NULL,
    user_id INT NOT NULL,
    stay_anonymous BOOLEAN DEFAULT TRUE,
    content TEXT NOT NULL,
    "timestamp" TIMESTAMP WITHOUT TIME ZONE DEFAULT (NOW())::TIMESTAMP WITHOUT TIME ZONE,
    rating INTEGER CONSTRAINT rating_range CHECK (rating >= 0 AND rating <=5)
);

CREATE TABLE cached_books(
    id BIGSERIAL PRIMARY KEY,
    book_id VARCHAR(150) UNIQUE NOT NULL,
    title VARCHAR(500),
    image_links JSON,
    categories JSON
);

CREATE TABLE cached_searches(
    id BIGSERIAL PRIMARY KEY,
    book_id VARCHAR(150) UNIQUE NOT NULL,
    "timestamp" TIMESTAMP WITHOUT TIME ZONE DEFAULT (NOW())::TIMESTAMP WITHOUT TIME ZONE,
    response JSON
);

CREATE TABLE events(
    id BIGSERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    performer INTEGER NOT NULL,
    target VARCHAR(150) NOT NULL,
    type VARCHAR(30) NOT NULL,
    "timestamp" TIMESTAMP WITHOUT TIME ZONE DEFAULT (NOW())::TIMESTAMP WITHOUT TIME ZONE
);

ALTER TABLE events
    ADD CONSTRAINT unique_event UNIQUE(user_id, performer, target, type);