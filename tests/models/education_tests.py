from nose.tools import *
from Human.api.models.education import Thesis, Degree

def test_thesis():
    t_data = {"title":"test", "summary":"test_summary"}
    th = Thesis(t_data)

    assert_true(isinstance(th, Thesis))
    assert_equal(th.title, "test")
    assert_equal(th.summary, "test_summary")

def test_thesis_without_title():
    t_data = {"summary":"test_summary"}
    th = Thesis(t_data)

    assert_equal(th.title, "")
    assert_equal(th.summary, "test_summary")


def test_thesis_without_summary():
    t_data = {"title":"test"}
    th = Thesis(t_data)

    assert_equal(th.title, "test")
    assert_equal(th.summary, "")

def test_degree():
    data = {
        "title": "test",
        "subject":"test_subject",
        "year": 2010,
        "thesis":{"title":"test", "summary":"test_summary"},
        "subjects":["Machine Learning"],
        "place":{"name":"Oslo"}
    }
    degree = Degree(data)

    assert_true(isinstance(degree, Degree))
    assert_equal(degree.title, "test")
    assert_equal(degree.subject, "test_subject")
    assert_equal(degree.year, 2010)
    assert_equal(degree.place.name, "Oslo")
    assert_true(len(degree.subjects) > 0)
    assert_equal(degree.thesis.title , "test")
    assert_equal(degree.thesis.summary , "test_summary")
