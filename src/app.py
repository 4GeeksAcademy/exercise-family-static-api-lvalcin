"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def get_all_members():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    return jsonify(members), 200

# GET /member/<int:member_id>

@app.route('/member/<int:id>', methods=['GET'])
def get_member(id):
    # this is how you can use the Family datastructure by calling its methods
    member = jackson_family.get_member(id)
    if member:
        # response_body = {
        #     "name": member["first_name"],
        #     "id": member["id"],
        #     "age": member["age"],
        #     "lucky_numbers":["lucky_members"]
        # }
        return jsonify(member), 200
    else:
        return jsonify({"error": "Member not found"}), 404


@app.route('/member', methods=['POST'])
def add_member():
    body = request.json 
    if not body:
        return jsonify({"error": "Missing request body"}), 400
    
    jackson_family.add_member(body)
    print(body, "Here is the BODYYYYY!!!!!!")
    return jsonify({"msg":"Member added succesfully"}), 200


@app.route('/member/<int:id>', methods=['DELETE'])
def delete_member(id):
    delete = jackson_family.delete_member(id)
    if delete:
        # body= {
        #  "done": True
        #     } 
        return jsonify({"done": True}), 200








# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
