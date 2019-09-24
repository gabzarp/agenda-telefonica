from flask import Flask, escape, request, json, jsonify
from flask_pymongo import PyMongo
import datetime

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/contacts"
mongo = PyMongo(app)


@app.route('/api/getContatos', methods=["GET"])
def getAllContacts():
    contacts = []
    for i in mongo.db.contacts.find():
        contacts.append({'id': str(i['_id']), 'name': i['name'] })
    return jsonify(contacts), 200


@app.route('/api/getContatoID/<ObjectId:id>', methods=["GET"])
def getContactById(id):
    contact = mongo.db.contacts.find_one_or_404({'_id': id })
    return jsonify({'id': str(contact['_id']) , 'name': contact['name'] }), 200


@app.route('/api/getContatoNome/<name>', methods=["GET"])
def getContactByName(name):
    contact = mongo.db.contacts.find_one_or_404({'name': {'$regex': name} })
    return jsonify({'id': str(contact['_id']) , 'name': contact['name'] }), 200


@app.route('/api/getContatoAniversario/<month>', methods=["GET"])
def getContactsByBirthMonth(month):
    contacts = []
    for i in mongo.db.contacts.find():
        if i['birthday'].month == int(month):
            contacts.append({ 'name': i['name'] })
    return jsonify(contacts), 200
