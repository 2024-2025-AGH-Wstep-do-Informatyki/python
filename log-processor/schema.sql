CREATE TABLE IF NOT EXISTS Logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME NOT NULL,
    ip TEXT NOT NULL,
    event_type TEXT NOT NULL,
    raw_event TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_logs_ip_timestamp ON Logs (ip, timestamp);

CREATE TABLE IF NOT EXISTS BlockedIPs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ip TEXT NOT NULL,
    block_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    unblock_time DATETIME,
    reason TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_blockedips_ip ON BlockedIPs (ip);
