import sys
import json

def isInteger(obj):
    try:
        int(obj)
        return True
    except ValueError:
        return False

def print_help():
    print("Invalid input provided\n \
    Pass path to JSON-formatted file as first argument and path to element in JSON file as second in format '/key/key' or '/key/number'\n \
    Example: python3 -m jq /home/docker/Documents/AWS/Connect/file.json '/object/items/2'\n \
    Note: path should start with '/'" 
    )
    

def read_file_as_json(path):
    with open(path, 'r') as file:
        text = file.read()
        return json.loads(text)

def find_element(obj, path):
    if not path:
        return None
    tmp = obj
    for elem in path:
        if not isInteger(elem):
            tmp = tmp[elem]
        else:
            tmp = tmp[int(elem)]
    
    return tmp
    

def main():
    if len(sys.argv) < 3:
        print_help()
        return

    path_to_file = sys.argv[1]
    path_to_element = sys.argv[2]
    if not path_to_element or path_to_element and path_to_element[0] != '/':
        print("Invalid path provided")
        return

    path_to_element_parsed = path_to_element.strip("/").split(sep='/')
    print(path_to_element_parsed)

    try:
        obj = read_file_as_json(path_to_file)
        res = find_element(obj, path_to_element_parsed) #discard first empty element in path
    except KeyError as err:
        print("Invalid key provided: {}".format(err))
    except IndexError as err:
        print("Invalid index provided: {}".format(err))
    except Exception as err:
        print("An error occured: {}".format(err))
    else:
        if res:
            print("Found the next element: {}".format(res))
        else:
            print("No element found by path '{}'".format(path_to_element))


