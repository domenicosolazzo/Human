class Contact(object):
    contact_type = None
    is_public = False
    def __init__(self, data):
        public = data.get('is_public', False)
        if isinstance(public, bool):
            self.is_public = public

    @staticmethod
    def get_instance(contact_type, optional_args):
        if contact_type == "email":
            return EmailContact(optional_args)



class EmailContact(Contact):
    email = None

    def __init__(self, data):
        super(EmailContact, self).__init__(data)
        self.email = data.get('email', '')
        self.contact_type = "email"
