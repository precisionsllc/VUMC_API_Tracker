# User Event Tracking API

The User Event Tracking API is a Flask-based web application that allows users to manage and track events in a MySQL database. Users can perform various operations such as creating, viewing, listing, and deleting events through the API.

## Prerequisites

Before running the API, ensure you have the following installed:

- Python
- Flask
- Flask-SQLAlchemy
- Flask-CORS
- MySQL server

You can install the required Python packages using `pip`. For example:

```bash
pip install flask flask_sqlalchemy flask_cors mysql-connector-python
```

## Setup

1. Clone the repository and navigate to the project directory.

2. Create a MySQL database and update the `mysql_config` dictionary in the `api_app.py` file with your MySQL server credentials and database name.

3. Run the API by executing the following command:

```bash
python3 api_app.py
```

The API will run on `http://127.0.0.1:5003`.

## Endpoints

### List Events

**URL:** `/events`

**Method:** GET

**Description:** Retrieve a list of all events in the database.

**Response:**

```json
[
    {
        "id": 1,
        "title": "Event Title 1",
        "description": "This is the description of Event 1.",
        "created_at": "2023-07-24 12:34:56"
    },
    {
        "id": 2,
        "title": "Event Title 2",
        "description": "This is the description of Event 2.",
        "created_at": "2023-07-24 13:45:12"
    },
    ...
]
```

### Create Event

**URL:** `/events`

**Method:** POST

**Description:** Create a new event with the given title and description.

**Request Body:**

```json
{
    "title": "New Event Title",
    "description": "This is a new event description."
}
```

**Response:**

```json
{
    "message": "Event created successfully",
    "event": {
        "id": 3,
        "title": "New Event Title",
        "description": "This is a new event description.",
        "created_at": "2023-07-24 14:56:23"
    }
}
```

### View Event

**URL:** `/events/{event_id}`

**Method:** GET

**Description:** Retrieve details of a specific event by its `event_id`.

**Response:**

```json
{
    "id": 1,
    "title": "Event Title 1",
    "description": "This is the description of Event 1.",
    "created_at": "2023-07-24 12:34:56"
}
```

### Delete Event

**URL:** `/events/{event_id}`

**Method:** DELETE

**Description:** Delete a specific event by its `event_id`.

**Response:**

```json
{
    "message": "Event deleted successfully"
}
```

### Search Events

**URL:** `/events/search?q={search_query}`

**Method:** GET

**Description:** Search for events with a title or description containing the given `search_query`.

**Response:**

```json
[
    {
        "id": 1,
        "title": "Event Title 1",
        "description": "This is the description of Event 1.",
        "created_at": "2023-07-24 12:34:56"
    },
    {
        "id": 3,
        "title": "New Event Title",
        "description": "This is a new event description.",
        "created_at": "2023-07-24 14:56:23"
    },
    
]
```

## Usage

You can interact with the User Event Tracking API using HTTP requests. For example, you can use Python's `requests` library to send HTTP requests to the API as shown in the example below:

```python
import requests

base_url = 'http://127.0.0.1:5003'

def list_events():
    response = requests.get(f'{base_url}/events')
    return response.json()

def create_event(title, description):
    data = {'title': title, 'description': description}
    response = requests.post(f'{base_url}/events', json=data)
    return response.json()

def view_event(event_id):
    response = requests.get(f'{base_url}/events/{event_id}')
    return response.json()

def delete_event(event_id):
    response = requests.delete(f'{base_url}/events/{event_id}')
    return response.json()

def search_events(query):
    response = requests.get(f'{base_url}/events/search?q={query}')
    return response.json()

if __name__ == '__main__':
    # Test the API functions here
    print("All Events:")
    events = list_events()
    print(events)

    new_event = create_event("New Event Title", "This is a new event description")
    print("New Event Created:")
    print(new_event)

    event_id = new_event.get('event').get('id

')
    print(f"Viewing Event ID {event_id}:")
    event = view_event(event_id)
    print(event)

    # Delete the newly created event
    delete_result = delete_event(event_id)
    print("Event Deleted:")
    print(delete_result)

    search_query = "New Event"
    print(f"Searching Events with '{search_query}' in title or description:")
    search_result = search_events(search_query)
    print(search_result)

    # Print all events again after creating a new event
    print("All Events After Creating New Event:")
    updated_events = list_events()
    print(updated_events)
```

Please note that you need to have the API running (`python3 api_app.py`) before making requests using the `api_client.py` script.

This README provides a brief overview of the User Event Tracking API and how to interact with it. You can extend the functionality and endpoints as per your project requirements.
