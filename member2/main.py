from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Sample data (in-memory storage)
data = {
    1: {'name': 'John', 'age': 25},
    2: {'name': 'Alice', 'age': 30}
}

# Create operation
@app.route('/create', methods=['POST'])
def create():
    if not request.json or 'name' not in request.json or 'age' not in request.json:
        return jsonify({'error': 'Invalid data format'}), 400

    new_id = max(data.keys()) + 1
    data[new_id] = {'name': request.json['name'], 'age': request.json['age']}
    return jsonify({'message': f'Record with ID {new_id} created'}), 201

# Read operation (Get all records)
@app.route('/read', methods=['GET'])
def read_all():
    return jsonify(data)

# Read operation (Get a specific record)
@app.route('/read/<int:id>', methods=['GET'])
def read(id):
    if id not in data:
        return jsonify({'error': 'Record not found'}), 404

    return jsonify(data[id])

# Update operation
@app.route('/update/<int:id>', methods=['PUT'])
def update(id):
    if id not in data:
        return jsonify({'error': 'Record not found'}), 404

    if not request.json or 'name' not in request.json or 'age' not in request.json:
        return jsonify({'error': 'Invalid data format'}), 400

    data[id]['name'] = request.json['name']
    data[id]['age'] = request.json['age']
    return jsonify({'message': f'Record with ID {id} updated'}), 200

# Delete operation
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    if id not in data:
        return jsonify({'error': 'Record not found'}), 404

    del data[id]
    return jsonify({'message': f'Record with ID {id} deleted'}), 200

# Serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
