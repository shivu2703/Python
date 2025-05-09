import csv
import json

def csv_to_json(csv_path, json_path ):
    with open(csv_path,'r') as csvfile:
        reader=csv.DictReader(csvfile)
        data= list(reader)

    with open(json_path,'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)


csv_to_json("./data.csv","./data.json")