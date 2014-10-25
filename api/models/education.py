from place import Place
class Degree(object):
    """
    Degree model that it represents a degree in the real world
    """
    title = ""
    subject = ""
    subjects=[]
    year = ""
    place = None
    thesis = None

    def __init__(self, data):
        if data is None:
            return None
        self.title = data.get('title', '')
        self.subject = data.get('subject', '')
        self.year = data.get('year', None)
        self.subjects = data.get('subjects', [])
        self.thesis = Thesis(data.get('thesis', None))

        place = data.get('place', None)
        if not place is None:
            self.place = Place(place)


class Thesis(object):
    """
    Thesis model
    """
    title = ""
    summary = ""

    def __init__(self, data):
        if data is None:
            return None
        self.title = data.get('title', '')
        self.summary = data.get('summary', '')