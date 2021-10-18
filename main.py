# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import json
import os
import sys
keys = []
dictionary = {}


def run_main():
    input_file = sys.argv[1]
    print(f"name of the script : {sys.argv[0]}")
    print(f"reading : {input_file}")
    if '.json' in input_file and check_file(input_file):
        json_file_reader(input_file)
        print(f"success")
    else:
        print('invalid input data file')


def check_file(file):
    try:
        return os.path.isfile(file)
    except FileNotFoundError as exception:
        print(exception)
    return False


def json_file_reader(data_file):
    # read object from data json file
    try:
        #with open('data/data_2.json') as jsonFile:
        with open(data_file) as jsonFile:
            data = json.load(jsonFile)
            message = data['message']
        recurse_message(message)
    except Exception as exception:
        print(exception)


def recurse_message(message):
    # recurse through the json object returned from json_file_reader()
    try:
        if type(message == dict):
            for k, v in message.items():
                if k not in keys:
                    if type(v) == str:
                        keys.append(k)
                        create_schema_obj(k, "string")
                    elif type(v) == int:
                        create_schema_obj(k, "integer")

                    elif type(v) == bool:
                        create_schema_obj(k, "boolean")

                    elif type(v) == list:
                        if len(v) > 0 and type(v[0]) == dict:
                            create_schema_obj(k, 'array')
                            recurse_message(v[0])
                        elif len(v) > 0 and type(v[0]) == str:
                            create_schema_obj(k, 'enum')
                        elif len(v) == 0:
                            create_schema_obj(k, "array")

                    elif type(v) == dict:
                        create_schema_obj(k, 'dict')
                        recurse_message(v)
            return write_obj(dictionary)
    except Exception as exception:
        print(exception)


def create_schema_obj(key, data_type):
    # Data to be written
    obj = {
        "type": data_type,
        "tag": "",
        "description": "",
        "required": False
    }
    dictionary.update({key: obj})


def write_obj(dictionary_obj):
    # write dictionary to schema json file
    try:
        schema_file = sys.argv[2]

        #with open("schema/schema_2.json", 'w') as outputFile:
        if '.json' in schema_file:
            with open(schema_file, 'w') as outputFile:
                json.dump(dictionary_obj, outputFile, indent=2)
        else:
            print('invalid output schema file')

            #print(f"{schema_file} SUCCESSFUL")
    except Exception as exception:
        print(exception)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #json_file_reader()
    run_main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
