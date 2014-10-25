from nose.tools import *
from Human.lib.models.person import Person

def test_person():
    data = {
        "education":[{"title":"Msc"}],
        "work_experience":[{"name":"abc"}],
        "firstname": "Domenico",
        "lastname":"Solazzo",
        "birthdate": "25/08/1982",
        "birthplace": {"name":"Asti"}
    }

    person = Person(data)
    assert_true(isinstance(person, Person))
    assert_equal(person.firstname, 'Domenico')
    assert_equal(person.lastname, 'Solazzo')
    assert_equal(person.birthdate, "25/08/1982")
    assert_equal(person.birthplace.name, "Asti")
    assert_equal(person.education[0].title, "Msc")
    assert_equal(person.work_experience[0].name, "abc")

