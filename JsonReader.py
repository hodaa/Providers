import json


class JsonReader:

    def read(self, file_name):
        with open('resources/' + file_name, 'r') as jsonFile:
            data = json.load(jsonFile)
        return data
