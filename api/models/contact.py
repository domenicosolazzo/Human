class Contact(object):
    contact_type = None
    def __init__(self):
        pass

class EmailContact(Contact):
    email = None

    def __init__(self, email):
        self.email = email
        self.contact_type = "email"