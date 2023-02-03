# CRUD API: A CRUD API allows clients to create, read, update, and delete resources. 
# Common problems that can arise while implementing a CRUD API include incorrect or incomplete data, data integrity issues, 
# and security concerns. To overcome these issues, proper validation and error handling should be implemented, 
# and a robust data storage solution should be used to ensure data integrity.

from flask import Flask, jsonify, request

app = Flask(__name__)

resources = [{'id': 1, 'data': 'Resource 1'},
             {'id': 2, 'data': 'Resource 2'}]

@app.route('/resources/<int:resource_id>', methods=['GET', 'PUT', 'DELETE'])
def resource_handler(resource_id):
    resource = [resource for resource in resources if resource['id'] == resource_id]
    if len(resource) == 0:
        return jsonify({'error': 'Resource not found'}), 404
    resource = resource[0]

    if request.method == 'GET':
        return jsonify(resource)
    elif request.method == 'PUT':
        resource.update(request.get_json())
        return jsonify(resource)
    elif request.method == 'DELETE':
        resources.remove(resource)
        return jsonify({'result': 'Resource deleted'})

@app.route('/resources/', methods=['POST'])
def create_resource():
    resource = request.get_json()
    resource['id'] = len(resources) + 1
    resources.append(resource)
    return jsonify(resource)

if __name__ == '__main__':
    app.run(debug=True)
