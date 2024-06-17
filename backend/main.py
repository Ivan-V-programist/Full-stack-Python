from flask import request, jsonify
from config import app, dataBase
from models import Contact

@app.route("/Contacts", methods=["GET"])
def getContacts():
    contacts = Contact.query.all()
    jsonContacts = list(map(lambda x:x.toJson(), contacts))
    
    return jsonify({"contacts":jsonContacts})

@app.route("/CreateContact", methods=["POST"])
def createContact():
    firstName = request.json.get("firstName")
    lastName = request.json.get("lastName")
    email = request.json.get("email")

    if not firstName or not lastName or not email:
        return (
            jsonify({"message": "Enter all credentials"}),
            400,
            )

    newContact = Contact(
            firstName=firstName, 
            lastName=lastName, 
            email=email
            )
    try:
        dataBase.session.add(newContact)
        dataBase.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400

    return jsonify({"message":"User Created"}), 201

@app.route("/updateContact/<int:userId>", methods=["PATCH"])
def updateContact(id):
    contact = Contact.query.get(id)

    if not contact:
        return jsonify({"message":"User Not Found"}), 404
    
    data = request.json
    contact.firstName = data.get("firstName", contact.firstName)
    contact.lastName = data.get("firstName", contact.lastName)
    contact.email = data.get("firstName", contact.email)

    dataBase.session.commit()
    return jsonify({"message": "User Updated"}), 200

@app.route("/deleteContact/<int:userId>", methods=["DELETE"])
def deleteContact(id):
    contact = Contact.query.get(id)

    if not contact:
        return jsonify({"message":"User Not Found"}), 404
    
    dataBase.session.delete(contact)
    dataBase.session.commit()

    return jsonify({"message": "User deleted"}), 200


if __name__ == "__main__":
    with app.app_context():
        dataBase.create_all()


    app.run(debug=True)