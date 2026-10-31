# Django REST API Learning Guide - Login API Example

## How REST APIs Work

A REST API (Representational State Transfer) is an architecture style that allows you to:
- Make requests to a server using HTTP methods (GET, POST, PUT, DELETE)
- Get JSON responses instead of HTML pages
- Build modern web applications with separate frontend and backend

### Key Concepts:

1. **Serializer**: Converts Python objects (like User) to/from JSON
2. **APIView**: A view class specifically for handling API requests
3. **Response**: Returns JSON data instead of HTML
4. **Status Codes**: HTTP status codes (200=success, 401=unauthorized, etc.)

---

## Testing the Login API

### Using JavaScript (Fetch API)

```javascript
// Login API call
fetch('/accounts/api/login/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
    },
    body: JSON.stringify({
        username: 'john',
        password: 'password123'
    })
})
.then(response => response.json())
.then(data => {
    console.log('Success:', data);
    // data will be:
    // {
    //     "message": "Login successful",
    //     "user": {
    //         "id": 1,
    //         "username": "john",
    //         "email": "john@example.com",
    //         "first_name": "John",
    //         "last_name": "Doe"
    //     }
    // }
})
.catch(error => console.error('Error:', error));
```

### Using cURL (Command Line)

```bash
curl -X POST http://127.0.0.1:8000/accounts/api/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"john","password":"password123"}'
```

### Using Postman

1. Open Postman
2. Create a new POST request to: `http://127.0.0.1:8000/accounts/api/login/`
3. Go to Body → Raw → JSON
4. Enter:
```json
{
    "username": "john",
    "password": "password123"
}
```
5. Click Send
6. You'll see the JSON response in the Response tab

### Using Python (requests library)

```python
import requests

response = requests.post(
    'http://127.0.0.1:8000/accounts/api/login/',
    json={
        'username': 'john',
        'password': 'password123'
    }
)

print(response.json())
# Output:
# {
#     'message': 'Login successful',
#     'user': {
#         'id': 1,
#         'username': 'john',
#         'email': 'john@example.com',
#         'first_name': 'John',
#         'last_name': 'Doe'
#     }
# }
```

---

## API Responses

### Successful Login (Status 200)
```json
{
    "message": "Login successful",
    "user": {
        "id": 1,
        "username": "john",
        "email": "john@example.com",
        "first_name": "John",
        "last_name": "Doe"
    }
}
```

### Failed Login (Status 401)
```json
{
    "message": "Login failed",
    "errors": {
        "non_field_errors": [
            "Invalid username or password"
        ]
    }
}
```

---

## How to See the API Call in Browser DevTools

1. Open DevTools (F12)
2. Go to **Network** tab
3. Check **Preserve log** checkbox
4. Make the API call (using fetch or form submission)
5. Look for the request to `/accounts/api/login/`
6. Click on it to see:
   - **Headers**: Request metadata
   - **Request**: The JSON data sent (username, password)
   - **Response**: The JSON response from server
   - **Timing**: How long the request took

---

## Differences Between Form-Based and REST API Login

### Form-Based Login (Original)
- Submits form as `application/x-www-form-urlencoded`
- Returns HTML page (302 redirect)
- Not visible as JSON in Network tab

### REST API Login (New)
- Sends JSON data
- Returns JSON response
- Visible in Network tab as API call
- Can be used by mobile apps, SPAs, etc.

---

## How It Works Under the Hood

1. **Client** sends POST request with username/password as JSON
2. **Django** receives the request
3. **LoginAPIView** processes it:
   - Serializer validates the data
   - `authenticate()` checks if username/password are correct
   - If correct, `auth.login()` creates a session
   - UserSerializer converts User object to JSON
4. **Server** returns JSON response
5. **Client** receives response and can display user info or redirect

---

## Next Steps to Learn

1. Add **Token Authentication** instead of session-based auth
2. Create a **Registration API** endpoint
3. Add **JWT tokens** for stateless authentication
4. Create **API permissions** to restrict access
5. Implement **CORS** to allow requests from different domains
