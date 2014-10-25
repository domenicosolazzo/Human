import os
import json
class DataSource(object):
    def __init__(self):
        pass

    @staticmethod
    def get_instance():
        data_source_type = os.environ.get('HUMAN_DATA_SOURCE_TYPE', "JSON")
        if data_source_type == "JSON":
            return JSONSource()
        else:
            raise Exception("Data source is not available")

    def fetch_person(self, id):
        raise Exception("Not implemented")

class JSONSource(DataSource):
    """
    Extract data from json files
    """
    def __init__(self):
        super(JSONSource, self).__init__()

    def fetch_person(self, id):
        person_file = '%s/data/%s.json' % (os.path.dirname(os.path.realpath(__file__)), id)
        try:
            with open(person_file) as f:
                person_json = json.load(f)
                return person_json
        except:
            raise Exception("Person not found")
