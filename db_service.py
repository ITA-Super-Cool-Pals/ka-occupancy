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


# Create a new occupancy
def create_occupancy(occupancy):
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute('INSERT INTO occupancy (BookingId, RoomId, GuestId, CheckIn) VALUES (?, ?, ?, ?)',
                    (occupancy['BookingId'], occupancy['RoomId'], occupancy['GuestId'], occupancy['CheckIn']))
    
    return True
        
    

# Update the check-out date for a specific occupancy
def update_occupancy(field, row_id):
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute('UPDATE occupancy SET CheckOut = ? WHERE RowId = ?', (field['CheckOut'], row_id))

    return True


def get_rooms():
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute('SELECT RoomId, GuestId FROM occupancy WHERE CheckOut IS NULL')
        rows = cur.fetchall()

        guests = requests.get('http://ka-guests:5000/guests').json()

        def get_guest_name(guest_id):
            for guest in guests:
                if guest['GuestId'] == guest_id:
                    return guest['Name']
            return 'Unknown'



        rooms = [{"RoomId": row[0], "GuestName": get_guest_name(row[1])} for row in rows]

    return rooms
    