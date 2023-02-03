#Read Only API: A Read Only API allows clients to retrieve resources without making any modifications. 
#Common problems that can arise while implementing a Read Only API include security concerns, data exposure, and poor performance due to frequent resource retrieval. To overcome these issues, 
#proper authentication and authorization should be implemented, and caching techniques can be used to improve performance.

from flask import Flask, jsonify

app = Flask(__name__)

resources = [{'id': 1, 'data': 'Resource 1'},
             {'id': 2, 'data': 'Resource 2'}]

@app.route('/resources/<int:resource_id>', methods=['GET'])
def get_resource(resource_id):
    resource = [resource for resource in resources if resource['id'] == resource_id]
    if len(resource) == 0:
        return jsonify({'error': 'Resource not found'}), 404
    return jsonify(resource[0])

if __name__ == '__main__':
    app.run(debug=True)
