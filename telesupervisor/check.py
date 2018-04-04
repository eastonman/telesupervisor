import api
import json


def write_database(data):
    db = open("db.py", 'w')
    json.dump(data, db)


def check_supervisor_process_status():
    api_data = api.getAllProcessInfo()
    data_json = {}
    old_data = read_database()
    new_data = api_data
    
    for process_data in api_data:
        name = process_data['name']
        statename = process_data['statename']
        data_json.update({name: statename})
    write_database(data_json)
    return 0


def read_database():    
    db = open("db.py", 'r')
    data = json.loads(db.read())
    return data
