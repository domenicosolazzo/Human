from place import Place
class Employer(object):
    """
    Employer model that represents a real work experience
    """
    from_date = ""
    to_date = ""
    place = None
    summary = "",
    name = ""
    title = ""
    sector = "",
    keywords = []

    def __init__(self, data):
        self.name = data.get('name', None)
        self.title = data.get('title', None)
        self.sector = data.get('sector', None)
        self.from_date = data.get('from_date', None)
        self.to_date = data.get('to_date', None)
        self.summary = data.get('summary', None)
        keywords = data.get('keywords', [])
        if not isinstance(keywords, list):
            keywords = []
        self.keywords = keywords

        place = data.get('place', None)
        if place is not None:
            self.place = Place(place)
