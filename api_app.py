

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS to allow cross-origin requests

# MySQL configuration
mysql_config = {
    'host': 'localhost',       # Use 'localhost' if the MySQL server is on the same machine
    'port': 3306,              # Port number for MySQL (default is 3306)
    'user': 'marklavine',      # Replace with your MySQL username
    'password': 'Crichlow_3381',  # Replace with your MySQL password
    'database': 'VUMC_Project',  # Replace with the name of your MySQL database
}

# Initialize the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqlconnector://{mysql_config['user']}:{mysql_config['password']}@{mysql_config['host']}:{mysql_config['port']}/{mysql_config['database']}"
db = SQLAlchemy(app)

# Define the Event model for the database table
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
        }

@app.route('/')
def index():
    return "Welcome to the User Event Tracking API!"

@app.route('/events', methods=['GET'])
def list_events():
    try:
        events = Event.query.all()
        return jsonify([event.to_dict() for event in events])
    except Exception as e:
        print(f"Error while retrieving events from the database: {e}")
        return jsonify({'error': 'Database error'}), 500

@app.route('/events', methods=['POST'])
def create_event():
    try:
        data = request.get_json()
        event = Event(title=data.get('title'), description=data.get('description'))
        db.session.add(event)
        db.session.commit()
        return jsonify({'message': 'Event created successfully', 'event': event.to_dict()})
    except Exception as e:
        db.session.rollback()
        print(f"Error while creating event: {e}")
        return jsonify({'error': 'Database error'}), 500

@app.route('/events/<int:event_id>', methods=['GET', 'PUT', 'DELETE'])
def event_detail(event_id):
    try:
        event = Event.query.get(event_id)
        if event is None:
            return jsonify({'message': 'Event not found'}), 404

        if request.method == 'GET':
            return jsonify(event.to_dict())
        elif request.method == 'PUT':
            data = request.get_json()
            if 'title' in data:
                event.title = data['title']
            if 'description' in data:
                event.description = data['description']
            db.session.commit()
            return jsonify({'message': 'Event updated successfully', 'event': event.to_dict()})
        elif request.method == 'DELETE':
            db.session.delete(event)
            db.session.commit()
            return jsonify({'message': 'Event deleted successfully'})

    except Exception as e:
        print(f"Error while handling event request: {e}")
        return jsonify({'error': 'Database error'}), 500

@app.route('/events/search', methods=['GET'])
def search_events():
    try:
        search_query = request.args.get('q', '')
        events = Event.query.filter(
            (Event.title.ilike(f'%{search_query}%')) | (Event.description.ilike(f'%{search_query}%'))
        ).all()
        return jsonify([event.to_dict() for event in events])
    except Exception as e:
        print(f"Error while searching events: {e}")
        return jsonify({'error': 'Database error'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)

