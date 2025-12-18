-- Tabla para los usuarios de la API
CREATE TABLE IF NOT EXISTS api_users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    username TEXT,
    email TEXT
);

CREATE TABLE IF NOT EXISTS api_todos (
    id INTEGER PRIMARY KEY,
    userId INTEGER,
    title TEXT,
    completed BOOLEAN,
    FOREIGN KEY (userId) REFERENCES api_users(id)
);

CREATE TABLE IF NOT EXISTS sistema_usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(100) UNIQUE,
    password_hash BLOB
);