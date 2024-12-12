import sqlite3
from datetime import datetime
from typing import List
from dataclasses import dataclass

DB_NAME = 'icantnamethings'

@dataclass
class Log:
    id: int
    timestamp: datetime
    ip: str
    event_type: str
    raw_event: str

class LogReader:
    def __init__(self, db_name: str):
        self.db_name = db_name

    def _connect(self):
        return sqlite3.connect(self.db_name + '.db')

    def get_all_logs(self) -> List[Log]:
        """Pobierz wszystkie logi z bazy danych."""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id, timestamp, ip, event_type, raw_event FROM Logs')
            rows = cursor.fetchall()
            return [Log(id=row[0], 
                        timestamp=datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S'), 
                        ip=row[2], 
                        event_type=row[3], 
                        raw_event=row[4]) for row in rows]

    def get_logs_by_ip(self, ip: str) -> List[Log]:
        """Pobierz logi dla danego adresu IP."""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id, timestamp, ip, event_type, raw_event FROM Logs WHERE ip = ?', (ip,))
            rows = cursor.fetchall()
            return [Log(id=row[0], 
                        timestamp=datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S'), 
                        ip=row[2], 
                        event_type=row[3], 
                        raw_event=row[4]) for row in rows]

    def get_logs_by_event_type(self, event_type: str) -> List[Log]:
        """Pobierz logi dla danego typu zdarzenia."""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id, timestamp, ip, event_type, raw_event FROM Logs WHERE event_type = ?', (event_type,))
            rows = cursor.fetchall()
            return [Log(id=row[0], 
                        timestamp=datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S'), 
                        ip=row[2], 
                        event_type=row[3], 
                        raw_event=row[4]) for row in rows]

if __name__ == "__main__":
    reader = LogReader(DB_NAME)

    print("--- Wszystkie logi ---")
    for log in reader.get_all_logs():
        print(log)

    print("\n--- Logi dla IP: 192.168.68.1 ---")
    for log in reader.get_logs_by_ip("192.168.68.1"):
        print(log)

    print("\n--- Logi dla zdarzenia typu: test ---")
    for log in reader.get_logs_by_event_type("test"):
        print(log)
