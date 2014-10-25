from nose.tools import *
from Human.api.models.place import Place

def test_place():
    data = {
        "lat":22,
        "lng":23,
        "name":"Oslo",
        "country":"Norway",
        "state":"Oslo",
        "zipcode":"1156"
    }

    place = Place(data)
    assert_true(isinstance(place, Place))
    assert_equal(place.name, "Oslo")
    assert_equal(place.country, "Norway")
    assert_equal(place.state, "Oslo")
    assert_equal(place.zipcode, "1156")
    assert_equal(place.lng, 23)
    assert_equal(place.lat, 22)

def test_place__without_lat():
    data = {
        "lng":23,
        "name":"Oslo",
        "country":"Norway",
        "state":"Oslo",
        "zipcode":"1156"
    }

    place = Place(data)
    assert_true(isinstance(place, Place))
    assert_equal(place.name, "Oslo")
    assert_equal(place.country, "Norway")
    assert_equal(place.state, "Oslo")
    assert_equal(place.zipcode, "1156")
    assert_equal(place.lng, 23)
    assert_equal(place.lat, None)


def test_place__without_lng():
    data = {
        "lat":23,
        "name":"Oslo",
        "country":"Norway",
        "state":"Oslo",
        "zipcode":"1156"
    }

    place = Place(data)
    assert_true(isinstance(place, Place))
    assert_equal(place.name, "Oslo")
    assert_equal(place.country, "Norway")
    assert_equal(place.state, "Oslo")
    assert_equal(place.zipcode, "1156")
    assert_equal(place.lng, None)
    assert_equal(place.lat, 23)


def test_place__without_zipcode():
    data = {
        "lng": 23,
        "lat":23,
        "name":"Oslo",
        "country":"Norway",
        "state":"Oslo"
    }

    place = Place(data)
    assert_true(isinstance(place, Place))
    assert_equal(place.name, "Oslo")
    assert_equal(place.country, "Norway")
    assert_equal(place.state, "Oslo")
    assert_equal(place.zipcode, None)
    assert_equal(place.lng, 23)
    assert_equal(place.lat, 23)


def test_place__without_state():
    data = {
        "lng": 23,
        "lat":23,
        "name":"Oslo",
        "country":"Norway",
        "zipcode":"1156"
    }

    place = Place(data)
    assert_true(isinstance(place, Place))
    assert_equal(place.name, "Oslo")
    assert_equal(place.country, "Norway")
    assert_equal(place.state, None)
    assert_equal(place.zipcode, "1156")
    assert_equal(place.lng, 23)
    assert_equal(place.lat, 23)


def test_place__without_country():
    data = {
        "lng": 23,
        "lat":23,
        "name":"Oslo",
        "state":"Oslo",
        "zipcode":"1156"
    }

    place = Place(data)
    assert_true(isinstance(place, Place))
    assert_equal(place.name, "Oslo")
    assert_equal(place.country, None)
    assert_equal(place.state, "Oslo")
    assert_equal(place.zipcode, "1156")
    assert_equal(place.lng, 23)
    assert_equal(place.lat, 23)


def test_place__without_zipcode():
    data = {
        "lng": 23,
        "lat":23,
        "country":"Norway",
        "state":"Oslo",
        "zipcode":"1156"
    }

    place = Place(data)
    assert_true(isinstance(place, Place))
    assert_equal(place.name, None)
    assert_equal(place.country, "Norway")
    assert_equal(place.state, "Oslo")
    assert_equal(place.zipcode, "1156")
    assert_equal(place.lng, 23)
    assert_equal(place.lat, 23)