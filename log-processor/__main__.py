import sqlite3
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

DB_NAME = 'icantnamethings'

@dataclass
class Log:
    id: Optional[int] = None
    timestamp: datetime = datetime.now()
    ip: str = ""
    event_type: str = ""
    raw_event: str = ""

def insert_log(conn, cursor, log: Log):
    cursor.execute('''
        INSERT INTO Logs (timestamp, ip, event_type, raw_event)
        VALUES (?, ?, ?, ?)
    ''', (log.timestamp.strftime('%Y-%m-%d %H:%M:%S'), log.ip, log.event_type, log.raw_event))
    conn.commit()
    log.id = cursor.lastrowid

def get_logs(cursor) -> [Log]:
    cursor.execute('SELECT id, timestamp, ip, event_type, raw_event FROM Logs')
    rows = cursor.fetchall()
    return [Log(id=row[0], timestamp=row[1], ip=row[2], event_type=row[3], raw_event=row[4]) for row in rows]

def get_logs_for_ip(cursor, ip: str) -> [Log]:
    cursor.execute('SELECT id, timestamp, ip, event_type, raw_event FROM Logs WHERE ip = ?', (ip,))
    rows = cursor.fetchall()
    return [Log(id=row[0], timestamp=row[1], ip=row[2], event_type=row[3], raw_event=row[4]) for row in rows]

@dataclass
class BlockedIP:
    id: Optional[int] = None
    ip: str = ""
    block_time: datetime = datetime.now()
    unblock_time: Optional[datetime] = None
    reason: str = ""

def insert_blocked_ip(conn, cursor, blocked_ip: BlockedIP):
    cursor.execute('''
        INSERT INTO BlockedIPs (ip, block_time, unblock_time, reason)
        VALUES (?, ?, ?, ?)
    ''', (blocked_ip.ip, blocked_ip.block_time.strftime('%Y-%m-%d %H:%M:%S'), blocked_ip.unblock_time.strftime('%Y-%m-%d %H:%M:%S') if blocked_ip.unblock_time else None, blocked_ip.reason))
    conn.commit()
    blocked_ip.id = cursor.lastrowid

def get_blocked_ips(cursor) -> [BlockedIP]:
    cursor.execute('SELECT id, ip, block_time, unblock_time, reason FROM BlockedIPs')
    rows = cursor.fetchall()
    return [BlockedIP(id=row[0], ip=row[1], block_time=row[2], unblock_time=row[3], reason=row[4]) for row in rows]

def is_ip_blocked(cursor, ip: str) -> bool:
    cursor.execute('SELECT COUNT(*) FROM BlockedIPs WHERE ip = ? AND (unblock_time IS NULL OR unblock_time < datetime("now"))', (ip,))
    return cursor.fetchone()[0] > 0


def init(conn, cursor):
    with open('schema.sql', 'r') as schema:
        sql_schema = schema.read()

    cursor.executescript(sql_schema)

    conn.commit()

    print("database and tables created")


def main():
    conn = sqlite3.connect(DB_NAME + '.db')
    cursor = conn.cursor()

    init(conn, cursor)

    log = Log(
        timestamp=datetime.now(),
        ip='192.168.68.1',
        event_type='test',
        raw_event='test event'
    )

    insert_log(conn, cursor, log)

    blocked_ip = BlockedIP(
        ip="192.168.68.1",
        block_time=datetime.now(),
        reason="test"
    )

    insert_blocked_ip(conn, cursor, blocked_ip)

    print(get_logs(cursor))
    print(get_logs_for_ip(cursor, "192.168.68.1"))

    print(get_blocked_ips(cursor))
    print(is_ip_blocked(cursor, "192.168.68.1"))
    print(is_ip_blocked(cursor, "192.168.68.2"))

    conn.close()

main()
