

import requests

base_url = 'http://127.0.0.1:5003'  # Replace with your Flask application's URL

def list_events():
    try:
        response = requests.get(f'{base_url}/events')
        response.raise_for_status()  # Check for any HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error while retrieving events: {e}")
        return None

def create_event(title, description):
    try:
        data = {'title': title, 'description': description}
        response = requests.post(f'{base_url}/events', json=data)
        response.raise_for_status()  # Check for any HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error while creating event: {e}")
        return None

def view_event(event_id):
    try:
        response = requests.get(f'{base_url}/events/{event_id}')
        response.raise_for_status()  # Check for any HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error while viewing event: {e}")
        return None

def delete_event(event_id):
    try:
        response = requests.delete(f'{base_url}/events/{event_id}')
        response.raise_for_status()  # Check for any HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error while deleting event: {e}")
        return None

def update_event(event_id, title=None, description=None):
    try:
        data = {}
        if title is not None:
            data['title'] = title
        if description is not None:
            data['description'] = description

        response = requests.put(f'{base_url}/events/{event_id}', json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error while updating event: {e}")
        return None

def search_events(query):
    try:
        response = requests.get(f'{base_url}/events/search?q={query}')
        response.raise_for_status()  # Check for any HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error while searching events: {e}")
        return None

if __name__ == '__main__':
    # Test the API functions here
    print("All Events:")
    events = list_events()
    if events:
        print(events)

    new_event = create_event("New Event Title", "This is a new event description")
    if new_event:
        print("New Event Created:")
        print(new_event)

        event_id = new_event.get('event').get('id')
        print(f"Viewing Event ID {event_id}:")
        event = view_event(event_id)
        if event:
            print(event)

        # Update the newly created event
        if event_id:
            updated_event = update_event(event_id, title="Updated Event Title", description="Updated Event Description")
            if updated_event:
                print("Event Updated:")
                print(updated_event)

        # Delete the newly created event
        if event_id:
            delete_result = delete_event(event_id)
            if delete_result:
                print("Event Deleted:")
                print(delete_result)

        search_query = "New Event"
        print(f"Searching Events with '{search_query}' in title or description:")
        search_result = search_events(search_query)
        if search_result:
            print(search_result)

        # Print all events again after creating a new event
        print("All Events After Creating New Event:")
        updated_events = list_events()
        if updated_events:
            print(updated_events)
