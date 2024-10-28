from flask import Flask
import db_service, requests


app = Flask(__name__)

@app.route('/')
def index():
    return 'Occupancy service'

if __name__ == '__main__':
    db_service.init()  # Ensure the database is initialized before running
    app.run(host='0.0.0.0')