import sqlite3, os, requests

db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'app-db', 'occu.db')
os.makedirs(os.path.dirname(db_path), exist_ok=True)

def init():
    # Ensure that the 'orders_data' directory exists


    with sqlite3.connect(db_path) as con:

        cur = con.cursor()

        cur.execute('''CREATE TABLE IF NOT EXISTS occupancy (
                    RowId INTEGER PRIMARY KEY AUTOINCREMENT,
                    BookingId INTEGER,
                    RoomId INTEGER,
                    GuestId INTEGER,
                    CheckIn DATETIME,
                    CheckOut DATETIME
                    )
                ''')
        
        cur.execute('SELECT COUNT(*) FROM occupancy')
        row_count = cur.fetchone()[0]
        
        if row_count == 0:
            cur.execute(''' INSERT INTO occupancy (BookingId, RoomId, GuestId, CheckIn, CheckOut) 
                        VALUES (1, 1, 1, '2021-06-01', '2021-06-03')
                        ''')
    con.commit()

def get_occupancies():
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute('SELECT * FROM occupancy')
        rows = cur.fetchall()

        occupancies = [{'RowId':row[0], 'BookingId':row[1], 'RoomId':row[2], 'GuestId': row[3], 'CheckIn':row[4], 'CheckOut':row[5]}for row in rows]
    
    return occupancies


def create_occupancy(occupancy):
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute('INSERT INTO occupancy (BookingId, RoomId, GuestId, CheckIn, CheckOut) VALUES (?, ?, ?, ?, ?)',
                    (occupancy['BookingId'], occupancy['RoomId'], occupancy['GuestId'], occupancy['CheckIn'], occupancy['CheckOut']))
        
def update_occupancy(field, row_id):
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute('UPDATE occupancy SET CheckOut = ? WHERE RowId = ?', (field['CheckOut'], row_id))

    