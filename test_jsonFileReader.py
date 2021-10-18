import json

import pytest

def test_jsonFile():

    with open('data/data_1.json') as jsonFile:
        data = json.load(jsonFile)
        message = data['message']

    with open("schema/schema_1.json") as inputFile:
        data2 = json.load(inputFile)
        schema_message = data2.keys()



    schema_keys = [message for message in schema_message]

    #add any key from data file to the list to verify it's existence on schema
    test_list = ['id', 'name', 'orientation', 'settings', 'status', 'creationTime', 'startTime', 'endTime', 'creator',
     'participants']
    assert all(item in schema_keys for item in test_list)
