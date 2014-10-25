from nose.tools import *
from human.core.api.human_facade import HumanFacade
from human.core.api.models.person import Person

def test_fetch_existing_person():
    human_id = "abc"
    facade = HumanFacade()
    person = facade.fetch_person(human_id)
    assert_true(isinstance(person, Person))

def test_fetch_not_existing_person():
    human_id = "not_exist"
    facade = HumanFacade()
    assert_raises(Exception, facade.fetch_person, human_id)