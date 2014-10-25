class Place(object):
    """
    Place model that represent a place in the real world
    """
    lat = ""
    lng = ""
    name = ""
    country = ""
    state = "",
    zipcode = ""

    def __init__(self, data):
        self.name = data.get('name', None)
        self.country = data.get('country', None)
        self.state = data.get('state', None)
        self.zipcode = data.get('zipcode', None)
        self.lat = data.get('lat', None)
        self.lng = data.get('lng', None)