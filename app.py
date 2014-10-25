from flask import Flask
from flask import jsonify
from human.rest.encoders.encoder import CustomJSONEncoder
from human.core.api.human_facade import HumanFacade

app = Flask(__name__)
app.json_encoder = CustomJSONEncoder

@app.route('/')
def hello_world():
    facade = HumanFacade()
    person = facade.fetch_person("abc")

    return jsonify(data=person)

if __name__ == '__main__':
    app.debug = True
    app.run()

