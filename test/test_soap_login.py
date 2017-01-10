
'''
def test_login(app):
    a = app.session.login("administrator", "root")
    b = app.soap.can_login("administrator", "root")
    assert a == b

def test_login(soap):

    ensure_if_login = soap.can_login("administrator", "root")

    assert ensure_if_login == ensure_if_login
'''
def test_login(app):

    app.soap.can_login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")

