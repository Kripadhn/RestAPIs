#Batch API: A Batch API allows clients to perform multiple operations in a single request, rather than making multiple 
#requests. This can improve performance and simplify the client implementation. Common problems that can arise while 
#implementing a Batch API include errors in individual operations leading to partial success, and difficulty in tracking 
#and managing errors. To overcome these issues, a robust error handling mechanism should be implemented, and the API should
# have the ability to return detailed results for each operation.
#Example in Python using Flask:

from flask import Flask, jsonify, request

app = Flask(__name__)

resources = [{'id': 1, 'data': 'Resource 1'},
             {'id': 2, 'data': 'Resource 2'}]

@app.route('/batch', methods=['POST'])
def batch_handler():
    operations = request.get_json()
    results = []

    for operation in operations:
        if operation['method'] == 'GET':
            resource = [resource for resource in resources if resource['id'] == operation['id']]
            if len(resource) == 0:
                results.append({'error': 'Resource not found'})
                continue
            results.append(resource[0])
        elif operation['method'] == 'PUT':
            resource = [resource for resource in resources if resource['id'] == operation['id']]
            if len(resource) == 0:
                results.append({'error': 'Resource not found'})
                continue
            resource = resource[0]
            resource.update(operation['data'])
            results.append(resource)
        elif operation['method'] == 'DELETE':
            resource = [resource for resource in resources if resource['id'] == operation['id']]
            if len(resource) == 0:
                results.append({'error': 'Resource not found'})
                continue resources.remove(resource[0])
                resources.remove(resource[0])
                results.append({'message': 'Resource deleted successfully'})
                else:
                results.append({'error': 'Invalid operation'})
            return jsonify(results)
        if name == 'main':
        app.run(debug=True)


        # These are the four most common types of REST APIs, each with its own specific use case and requirements. 
        # It's important to choose the right type of API for your specific use case, and to implement it with care to 
        # ensure performance, reliability, and security.

