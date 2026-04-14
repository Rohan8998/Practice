import requests
import json

def test_get_users():
    # 1. Define the API endpoint URL (we use JSONPlaceholder, a free fake API for testing)
    url = "https://jsonplaceholder.typicode.com/users/1"
    
    # 2. Send the GET request
    response = requests.get(url)

    
    # 3. Print the results to the terminal so we can see what the API returned
    print("\n--- API Response Info ---")
    print(f"Status Code: {response.status_code}")
    print(f"Response JSON: {response.json()}")
    print("-------------------------")

    with open('user_data.json', 'w') as file:
        json.dump(response.json(), file, indent=4)
        print("Data saved to user_data.json")

    data = response.json()
    assert data['name'] == 'Leanne Graham'
    assert data['email'] == 'Sincere@april.biz'
    assert data['address']['city'] == 'Gwenborough'
    # 4. Add an assertion to check that the request was successful
    # Status code 200 means "OK"
    assert response.status_code == 200





def test_create_user():
    # 1. Provide the URL to the 'users' endpoint
    url = "https://jsonplaceholder.typicode.com/users"
    
    # 2. Define the payload (the data we want to send)
    payload = {
        "name": "Rohan Tester",
        "username": "rohan_t",
        "email": "rohan.testing@example.com",
        "address": {
            "street": "Balaji Nagar",
            "suite": "Aarti Apt",
            "city": "Pune",
            "zipcode": "411043",
            "geo": {
                "lat": "18.5204",
                "lng": "73.8567"
            }
        },
        "Hometown":"Pune"
    }
    
    # 3. Send the POST request. Notice we use requests.post() and pass 'json=payload'
    response = requests.post(url, json=payload)
    
    print("\n--- POST Response Info ---")
    print(f"Status Code: {response.status_code}")
    print(f"Response JSON: {response.json()}")
    
    # 4. Assertions
    # Status code 201 means "Created" (standard for successful POST requests)
    assert response.status_code == 201
    
    # 5. Validate that the API returns an 'id' for our new user
    data = response.json()
    assert "id" in data
    assert data["name"] == "Rohan Tester"
    assert data["address"]["city"] == "Pune"
    assert data["address"]["zipcode"] == "411043"
    assert data["Hometown"] == "Pune"


