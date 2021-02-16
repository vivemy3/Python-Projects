import json
import os.path


filename = "amdb.json"

#Reads the JSON file
def readjson():
    try:
        with open(filename) as datasheet:
            info = json.load(datasheet)

    except json.decoder.JSONDecodeError:
        msg = "\nCan't find {0}\n".format(filename)
        return(msg)
    else:
        return  info

#Writes to the JSON file
def writejson(key, value):
    try:
        with open(filename) as datasheet:
            xdict = json.load(datasheet)

    except json.decoder.JSONDecodeError:
        data = {key:value}
        with open(filename, "w") as info:
            json.dump(data, info)


    else:
        xdict[key]=value
        with open(filename, "w") as info:
            json.dump(xdict, info)


#Deletes info from the JSON file
def deletejsoninfo(key):
    with open(filename) as datasheet:
        xdict = json.load(datasheet)

    del xdict[key]

    with open(filename, "w") as info:
        json.dump(xdict, info)

# Gets and sorts data from the JSON file to show in the Listbox
def populateListbox():
    lst = [readjson().values()]
    for item in lst:
        return(item)

def counter():
    lst = [readjson().values()]
    for item in lst:
        number =str(len(item))
    return(number)





