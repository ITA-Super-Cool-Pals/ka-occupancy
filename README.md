# ka-occuppancy
Occupancy microservice for Hotel Kong Arthur

```
docker build -t ka-occupancy
```

```
docker run --rm -p 5005:5000 -v ./ka-app:/app/app-db --name -ka-reviews -d ka-reviews
```

## API Endpoints
### Se alle data points
 - **URL:** `/occupancy`
 - **Method**: `GET`
 - **Response**
    - **200 OK**: Returns all entries

### Lav en ny occupancy
   - **URL:** `/occupancy`
   - **MEthod:** `POST`
   - **Request Body:**
   ```
   {
    "BookingId": <booking_id>,
    "RoomId": <room_id>,
    "GuestId": <guest_id>,
    "CheckIn": <date_format yyyy-mm-dd>
   }
   ```

   Checkout happens in another endpoint.

   - **Response:**
      - **201 OK:** Occupancy created


### Update Occupancy
   - **URL:** `/occupancy/<id>`
   - **MEthod:** `PATCH`
   - **Request Body:**
   ```
   {
    "CheckOut": <date_format yyyy-mm-dd>
   }
   ```
    - **Response:**
        - **200 OK:** Occupancy updated

### List all occupied rooms
 - **URL:** `/occupancy/rooms`
 - **Method**: `GET`
 - **Response**
    - **200 OK**: Returns all entries

