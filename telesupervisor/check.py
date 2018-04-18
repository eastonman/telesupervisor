import api
import json
import pickle

def write_database(data):
    db = open("db.json", 'w')
    json.dump(data, db)


def check_supervisor_process_status():
    api_data = api.getAllProcessInfo()
    data_json = {}
    new_data_json = {}
    old_data = read_database()
    new_data = api_data
    for new_process_data in new_data:
        name = new_process_data['name']
        statename = new_process_data['statename']
        new_data_json.update({name: statename})
    if old_data == '':
        pass
    else:
        for process_name in old_data:
            if old_data[process_name] == new_data_json[process_name]:
                pass
            else:
                print('Status Changed')
    for process_data in api_data:
        name = process_data['name']
        statename = process_data['statename']
        data_json.update({name: statename})
    write_database(data_json)
    return 0


def read_database(): 
    try:
        db = open("db.pkl", 'r')
    except IOError:
        logging.warning('File db.json is not accessible.')
        db = open("db.pkl", 'w')
        db.close()
        logging.warning('Automatically create db.json')
        return 1
    try:
        data = pickle.load(db)
    except:
        return ''
    return data
