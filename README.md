# VUMC_API_Tracker

# VUMC Event Tracking API


Requirements
Python 3.6+
Flask
Flask SQLAlchemy
Flask-CORS
MySQL server

## Setup
1. Install the required dependencies:
```bash
pip install Flask Flask-SQLAlchemy Flask-CORS
```
2. Set up your MySQL server and create a database named `VUMC_Project`. Replace the
credentials in the `api_app.py` file with your MySQL username and password.

## Description

The VUMC Event Tracking API is a Flask-based web application that allows users to track events. It provides endpoints for listing events, creating new events, viewing specific events, and searching for events based on their title or description. The API is backed by a MySQL database to store event data.

## Architecture

The application follows a client-server architecture. The server-side is implemented using Flask, a Python web framework, which handles HTTP requests and responses. The server communicates with a MySQL database to store and retrieve event data.

The client-side is a separate Python script, `api_client.py`, which interacts with the API endpoints to perform various actions, such as listing events, creating new events, viewing event details, and searching for events.

## Installation

To get the application running locally, follow these steps:

1. Clone the repository to your local machine:
   ```
   git clone <repository_url.git>
   ```

2. Install the required dependencies. Navigate to the project directory and create a virtual environment (optional but recommended):
   ```
   cd vumc_api_event_tracker
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

4. Configure MySQL database settings:
   - Open `api_app.py` and modify the `mysql_config` dictionary with your MySQL database credentials.

5. Run the API server:
   ```
   python3 api_app.py
   ```

6. Open a new terminal window and run the API client script:
   ```
   python3 api_client.py
   ```

The API client will perform various interactions with the API and display the results in the terminal.

## Interaction Examples

### Listing All Events:

```bash
python3 api_client.py
```

Output:
```
All Events:
[
    {
        'id': 1,
        'title': 'Event 1',
        'description': 'Description of Event 1',
        'created_at': '2023-07-20 10:00:00'
    },
    {
        'id': 2,
        'title': 'Event 2',
        'description': 'Description of Event 2',
        'created_at': '2023-07-20 12:00:00'
    },
    ...
]
```

### Creating a New Event:

```bash
python3 api_client.py
```

Output:
```
New Event Created:
{
    'message': 'Event created successfully',
    'event': {
        'id': 10,
        'title': 'New Event Title',
        'description': 'This is a new event description',
        'created_at': '2023-07-21 15:30:00'
    }
}
```

### Viewing Event Details:

```bash
python3 api_client.py
```

Output:
```
Viewing Event ID 1:
{
    'id': 1,
    'title': 'Event 1',
    'description': 'Description of Event 1',
    'created_at': '2023-07-20 10:00:00'
}
```

### Searching Events:

```bash
python3 api_client.py
```

Output:
```
Searching Events with 'Event' in title or description:
[
    {
        'id': 1,
        'title': 'Event 1',
        'description': 'Description of Event 1',
        'created_at': '2023-07-20 10:00:00'
    },
    {
        'id': 2,
        'title': 'Event 2',
        'description': 'Description of Event 2',
        'created_at': '2023-07-20 12:00:00'
    },
    ...
]
