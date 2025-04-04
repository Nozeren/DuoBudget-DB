CREATE TABLE IF NOT EXISTS banks(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    country TEXT NOT NULL,
    color TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS users(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    color TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS categories(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS subcategories(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    category_id INT NOT NULL REFERENCES categories (id)
);

CREATE TABLE IF NOT EXISTS transactions(
    id SERIAL PRIMARY KEY,
    posted_date DATE NOT NULL,
    description TEXT NOT NULL,
    user_id INT NOT NULL REFERENCES users (id),
    subcategory_id INT REFERENCES subcategories (id),
    bank_id INT NOT NULL REFERENCES banks (id),
    shared_amount decimal(12, 2) NOT NULL DEFAULT 0,
    amount decimal(12, 2) NOT NULL
);

CREATE TABLE IF NOT EXISTS temporary_transactions(
    id SERIAL PRIMARY KEY,
    posted_date DATE NOT NULL,
    description TEXT NOT NULL,
    user_id INT NOT NULL REFERENCES users (id),
    subcategory_id INT REFERENCES subcategories (id),
    bank_id INT NOT NULL REFERENCES banks (id),
    shared_amount decimal(12, 2) NULL DEFAULT 0,
    amount decimal(12, 2) NOT NULL
);

CREATE TABLE IF NOT EXISTS budget(
    id SERIAL PRIMARY KEY,
    month INT NOT NULL,
    year INT NOT NULL,
    user_id INT NOT NULL REFERENCES users (id),
    subcategory_id INT REFERENCES subcategories (id),
    assigned decimal(12, 2) NOT NULL DEFAULT 0,
    activity decimal(12, 2) NOT NULL DEFAULT 0,
    available decimal(12, 2) NOT NULL DEFAULT 0
);