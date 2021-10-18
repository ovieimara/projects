# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import json
import pickle
import pprint
#from test_jsonFileReader import test_jsonFile

duplicates = []
dictionary = {}
def jsonFileReader():

    with open('data/data_2.json') as jsonFile:
        data = json.load(jsonFile)
        message = data['message']
    print(message.keys())
    #print(message['user'].keys())
    recurseMessage(message)

def recurseMessage(message):
    try:
        if type(message == dict):
            for k, v in message.items():
                if k not in duplicates:
                    if type(v) == str:
                        # pprint.pprint(i)
                        duplicates.append(k)
                        createSchemaObj(k, "string")
                    elif type(v) == int:
                        # pprint.pprint(i)
                        createSchemaObj(k, "integer")

                    elif type(v) == bool:
                        createSchemaObj(k, "boolean")

                    elif type(v) == list:
                        if len(v) > 0 and type(v[0]) == dict:
                            #print(v[0])
                            createSchemaObj(k, 'array')
                            recurseMessage(v[0])
                            data_type = 'array'
                        elif len(v) > 0 and type(v[0]) == str:
                            createSchemaObj(k, 'enum')
                        elif len(v) == 0:
                            createSchemaObj(k, "array")

                    elif type(v) == dict:
                        # pprint.pprint(i[1])
                        # createSchemaObj(i[0], "enum")
                        #pprint.pprint(v)
                        createSchemaObj(k, 'dict')
                        recurseMessage(v)
        return writeObj(dictionary)
    except Exception as exception:
        print(exception)


def createSchemaObj(key, dataType):
    # Data to be written
    obj = {
        "type": dataType,
        "tag": "",
        "description": "",
        "required": "false"
    }
    dictionary.update({key: obj})
    #print(dictionary.items())
    #dicset = [{str(k), str(v)} for k, v in dictionary.items()]
    #dic='\n'.join(dictionary.items())
    #print(dic)
    #a = "".join(f"{k}: {v}," for k, v in dictionary.items())
    #print(a)

def writeObj(a):

    with open("schema/schema_2.json", 'w') as outputFile:
        #outputFile.write("\n\n\n\n")
        json.dump(a, outputFile, indent=2)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    jsonFileReader()
    #test_jsonFile()

    #print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
