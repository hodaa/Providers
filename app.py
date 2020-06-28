import flask
from flask import jsonify, request
from os import listdir
from os.path import isfile, join
from ProvidersFactory import ProvidersFactory
from JsonReader import JsonReader

app = flask.Flask(__name__)
app.config["DEBUG"] = False


@app.route('/', methods=['GET'])
def home():
    return "home page"


@app.route('/api/v1/providers', methods=['GET'])
def get_providers_data():
    result = get_data()
    filtered = []
    if 'provider' in request.args:
        provider = request.args['provider']
        for item in result:
            if item['provider'] == provider:
                filtered.append(item)

    if 'statusCode' in request.args:
        for item in result:
            if item['status'] == request.args['statusCode']:
                filtered.append(item)

    else:
        filtered = result

    return jsonify(filtered)


def get_data():
    result = []
    files = [f for f in listdir('resources') if isfile(join('resources', f))]
    for file in files:
        provider_obj = ProvidersFactory.create(file)
        data = JsonReader().read(file)
        result.append(provider_obj.parse(data))
    return result


app.run()
