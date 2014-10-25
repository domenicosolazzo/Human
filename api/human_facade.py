from sources.datasources import DataSource
from models.person import Person

class HumanFacade(object):
    """
    Layer for the business logic and retrieving the data from the data layer
    """
    __data_adapter = None

    def __init__(self):
        self.__data_adapter = DataSource.get_instance()

    def fetch_person(self, id):
        try:
            data = self.__data_adapter.fetch_person(id)
            person = Person(data)
            return person
        except:
            raise Exception("Person not found")