CREATE TABLE users(
id BIGSERIAL PRIMARY KEY,
first_name VARCHAR(100),
last_name VARCHAR(100),
discriminator INTEGER CONSTRAINT integer_range CHECK (discriminator >= 1000 AND discriminator <= 9999),
username VARCHAR(500),
email VARCHAR(255) NOT NULL UNIQUE,
avatar_url text,
followers json DEFAULT '[]',
following json DEFAULT '[]'
);

ALTER TABLE users
    ADD CONSTRAINT username UNIQUE(first_name, last_name, discriminator);

CREATE TABLE reviews(
    id BIGSERIAL PRIMARY KEY,
    book_id VARCHAR(150) NOT NULL,
    user_id INT NOT NULL,
    stay_anonymous BOOLEAN DEFAULT TRUE,
    content TEXT NOT NULL,
    "timestamp" TIMESTAMP WITHOUT TIME ZONE DEFAULT (NOW())::TIMESTAMP WITHOUT TIME ZONE,
    rating INTEGER CONSTRAINT rating_range CHECK (rating >= 0 AND rating <=5)
);