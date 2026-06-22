CREATE TABLE incidents (
    id SERIAL PRIMARY KEY,
    severity VARCHAR(50),
    issue TEXT,
    recommendation TEXT,
    action_taken TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);