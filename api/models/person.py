from work_experience import Employer
from education import Degree
from place import Place
from contact import Contact
class Person(object):
    """
    Person model
    """
    education = []
    work_experience = []
    firstname = ""
    lastname = ""
    birthdate = ""
    birthplace = ""
    contacts = []

    def __init__(self, data):
        self.__initialization(data)

    def __initialization(self, data):
        if data is None:
            raise Exception("Data is invalid")

        self.firstname = data.get('firstname', None)
        self.lastname = data.get('lastname', None)
        self.birthdate = data.get('birthdate', None)
        birthplace = data.get('birthplace', None)
        if birthplace is not None:
            self.birthplace = Place(birthplace)

        employers = data.get('work_experience', [])
        if isinstance(employers, list):
            for employer in employers:
                self.work_experience.append(
                    Employer(employer)
                )

        degrees = data.get('education', [])
        if isinstance(degrees, list):
            for degree in degrees:
                self.education.append(Degree(degree))

        contacts = data.get('contacts', [])
        if isinstance(contacts, list):
            for contact in contacts:
                self.contacts.append(Contact.get_instance(data))





