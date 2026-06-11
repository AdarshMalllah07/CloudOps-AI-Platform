CREATE TABLE environments (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE servers (
    id SERIAL PRIMARY KEY,
    environment_id INTEGER REFERENCES environments(id),
    hostname VARCHAR(255) NOT NULL,
    ip_address VARCHAR(50),
    operating_system VARCHAR(100),
    status VARCHAR(50) DEFAULT 'ACTIVE',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE applications (
    id SERIAL PRIMARY KEY,
    server_id INTEGER REFERENCES servers(id),
    name VARCHAR(255) NOT NULL,
    version VARCHAR(50),
    status VARCHAR(50) DEFAULT 'RUNNING',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);