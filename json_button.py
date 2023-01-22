from flask import jsonify, request

# JSON-Button Methode
def json_response():
    """
    Handle a request from the client when the "JSON" button is clicked.

    Returns:
        str: A JSON string containing the data from the request form.
    """
    # Get the data from the request form as a dictionary
    data = request.form.to_dict()

    # Remove the "submit" and "name" keys from the dictionary
    del data["submit"]
    del data["name"]

    # Return the dictionary as a JSON string
    return jsonify(data)