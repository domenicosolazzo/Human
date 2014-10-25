from nose.tools import *
from Human.api.models.contact import Contact, EmailContact

"""
Email Contact
"""
def test_email_contact():
    email = "abc@example.com"
    email_contact = Contact.get_instance("email", {"email": email})
    assert_true(isinstance(email_contact, EmailContact))
    assert_equal(email, email_contact.email)
    assert_false(email_contact.is_public)

def test_email_contact_is_public():
    email = "abc@example.com"
    email_contact = Contact.get_instance("email", {"email": email, "is_public":True})
    assert_true(email_contact.is_public)
