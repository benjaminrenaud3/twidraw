import os
import json
import string

def create_file(path: string, data: string):
    """
    Check if file exist and delete it
    Create a file with json content
    ARg:
        - path : path to create file ("result/file.json")
        - data : content of file. Necessary string in json format
    """

    if os.path.exists(path):
        os.remove(path)
    file1 = open(path, "a")
    file1.write(json.dumps(data, indent=4, sort_keys=True))
    file1.close()



if __name__ == '__main__':
    create_file("./default.json", "ok")