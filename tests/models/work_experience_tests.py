from nose.tools import *
from Human.api.models.work_experience import Employer, Place

def test_employer():
    data = {
        "name": "abc",
        "from_date": "25/08/1982",
        "to_date":"26/08/1982",
        "summary": "This is a summary",
        "name": "abc",
        "title": "Developer",
        "sector": "Healthcare",
        "keywords": ["Python"],
        "place": {"name":"Oslo"}
    }

    employer = Employer(data)
    assert_true(isinstance(employer, Employer))
    assert_equal(employer.from_date, "25/08/1982")
    assert_equal(employer.to_date, "26/08/1982")
    assert_equal(employer.summary, "This is a summary")
    assert_equal(employer.name, "abc")
    assert_equal(employer.title,"Developer" )
    assert_equal(employer.sector, "Healthcare")
    assert_equal(employer.keywords, ["Python"])
    assert_equal(employer.place.name, "Oslo")

def test_employer__without_name():
    data = {
        "from_date": "25/08/1982",
        "to_date":"26/08/1982",
        "summary": "This is a summary",
        "title": "Developer",
        "sector": "Healthcare",
        "keywords": ["Python"],
        "place": {"name":"Oslo"}
    }

    employer = Employer(data)
    assert_true(isinstance(employer, Employer))
    assert_equal(employer.from_date, "25/08/1982")
    assert_equal(employer.to_date, "26/08/1982")
    assert_equal(employer.summary, "This is a summary")
    assert_equal(employer.name, None)
    assert_equal(employer.title,"Developer" )
    assert_equal(employer.sector, "Healthcare")
    assert_equal(employer.keywords, ["Python"])
    assert_equal(employer.place.name, "Oslo")

def test_employer__without_from_date():
    data = {
        "name": "abc",
        "to_date":"26/08/1982",
        "summary": "This is a summary",
        "name": "abc",
        "title": "Developer",
        "sector": "Healthcare",
        "keywords": ["Python"],
        "place": {"name":"Oslo"}
    }

    employer = Employer(data)
    assert_true(isinstance(employer, Employer))
    assert_equal(employer.from_date, None)
    assert_equal(employer.to_date, "26/08/1982")
    assert_equal(employer.summary, "This is a summary")
    assert_equal(employer.name, "abc")
    assert_equal(employer.title,"Developer" )
    assert_equal(employer.sector, "Healthcare")
    assert_equal(employer.keywords, ["Python"])
    assert_equal(employer.place.name, "Oslo")

def test_employer__without_to_date():
    data = {
        "name": "abc",
        "from_date": "25/08/1982",
        "summary": "This is a summary",
        "name": "abc",
        "title": "Developer",
        "sector": "Healthcare",
        "keywords": ["Python"],
        "place": {"name":"Oslo"}
    }

    employer = Employer(data)
    assert_true(isinstance(employer, Employer))
    assert_equal(employer.from_date, "25/08/1982")
    assert_equal(employer.to_date, None)
    assert_equal(employer.summary, "This is a summary")
    assert_equal(employer.name, "abc")
    assert_equal(employer.title,"Developer" )
    assert_equal(employer.sector, "Healthcare")
    assert_equal(employer.keywords, ["Python"])
    assert_equal(employer.place.name, "Oslo")

def test_employer__without_summary():
    data = {
        "name": "abc",
        "from_date": "25/08/1982",
        "to_date":"26/08/1982",
        "name": "abc",
        "title": "Developer",
        "sector": "Healthcare",
        "keywords": ["Python"],
        "place": {"name":"Oslo"}
    }

    employer = Employer(data)
    assert_true(isinstance(employer, Employer))
    assert_equal(employer.from_date, "25/08/1982")
    assert_equal(employer.to_date, "26/08/1982")
    assert_equal(employer.summary, None)
    assert_equal(employer.name, "abc")
    assert_equal(employer.title,"Developer" )
    assert_equal(employer.sector, "Healthcare")
    assert_equal(employer.keywords, ["Python"])
    assert_equal(employer.place.name, "Oslo")

def test_employer__without_title():
    data = {
        "name": "abc",
        "from_date": "25/08/1982",
        "to_date":"26/08/1982",
        "summary": "This is a summary",
        "name": "abc",
        "sector": "Healthcare",
        "keywords": ["Python"],
        "place": {"name":"Oslo"}
    }

    employer = Employer(data)
    assert_true(isinstance(employer, Employer))
    assert_equal(employer.from_date, "25/08/1982")
    assert_equal(employer.to_date, "26/08/1982")
    assert_equal(employer.summary, "This is a summary")
    assert_equal(employer.name, "abc")
    assert_equal(employer.title,None)
    assert_equal(employer.sector, "Healthcare")
    assert_equal(employer.keywords, ["Python"])
    assert_equal(employer.place.name, "Oslo")

def test_employer__without_sector():
    data = {
        "name": "abc",
        "from_date": "25/08/1982",
        "to_date":"26/08/1982",
        "summary": "This is a summary",
        "name": "abc",
        "title": "Developer",
        "keywords": ["Python"],
        "place": {"name":"Oslo"}
    }

    employer = Employer(data)
    assert_true(isinstance(employer, Employer))
    assert_equal(employer.from_date, "25/08/1982")
    assert_equal(employer.to_date, "26/08/1982")
    assert_equal(employer.summary, "This is a summary")
    assert_equal(employer.name, "abc")
    assert_equal(employer.title,"Developer" )
    assert_equal(employer.sector, None)
    assert_equal(employer.keywords, ["Python"])
    assert_equal(employer.place.name, "Oslo")

def test_employer__without_keywords():
    data = {
        "name": "abc",
        "from_date": "25/08/1982",
        "to_date":"26/08/1982",
        "summary": "This is a summary",
        "name": "abc",
        "title": "Developer",
        "sector": "Healthcare",
        "place": {"name":"Oslo"}
    }

    employer = Employer(data)
    assert_true(isinstance(employer, Employer))
    assert_equal(employer.from_date, "25/08/1982")
    assert_equal(employer.to_date, "26/08/1982")
    assert_equal(employer.summary, "This is a summary")
    assert_equal(employer.name, "abc")
    assert_equal(employer.title,"Developer" )
    assert_equal(employer.sector, "Healthcare")
    assert_equal(employer.keywords, [])
    assert_equal(employer.place.name, "Oslo")

def test_employer__without_place():
    data = {
        "name": "abc",
        "from_date": "25/08/1982",
        "to_date":"26/08/1982",
        "summary": "This is a summary",
        "name": "abc",
        "title": "Developer",
        "sector": "Healthcare",
        "keywords": ["Python"]
    }

    employer = Employer(data)
    assert_true(isinstance(employer, Employer))
    assert_equal(employer.from_date, "25/08/1982")
    assert_equal(employer.to_date, "26/08/1982")
    assert_equal(employer.summary, "This is a summary")
    assert_equal(employer.name, "abc")
    assert_equal(employer.title,"Developer" )
    assert_equal(employer.sector, "Healthcare")
    assert_equal(employer.keywords, ["Python"])
    assert_equal(employer.place, None)

def test_employer__keywords_must_be_a_list():
    data = { "keywords": 1 }
    employer = Employer(data)
    assert_equal(employer.keywords, [])

    data = {"keywords": True}
    employer = Employer(data)
    assert_equal(employer.keywords, [])

    data = {"keywords": "string"}
    employer = Employer(data)
    assert_equal(employer.keywords, [])

    data = {"keywords": ["Python"]}
    employer = Employer(data)
    assert_equal(employer.keywords, ["Python"])








