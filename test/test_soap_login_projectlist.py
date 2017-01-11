from model.project import Project
import random
import string

'''
def test_login(app): #1) работает
    a = app.session.login("administrator", "root")
    b = app.soap.can_login("administrator", "root")
    assert a == b

def test_login(soap): # 2) не работает

    ensure_if_login = soap.can_login("administrator", "root")

    assert ensure_if_login == ensure_if_login
'''
def test_login(app): # 3)  работает

    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")
'''
def test_login(app): # 4) не работает

    app.soap.can_login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")

'''
def test_add_project(app):

    project = Project(name=random_string(5), description=random_string(10)) #создаем проект
    old_projects_soap = app.soap.get_list_of_projects() # получаем список пректов через API
    app.project.create_project(project)
    new_projects_soap = app.soap.get_list_of_projects()
    old_projects_soap.append(project)
    assert sorted(old_projects_soap, key=lambda x: x.name) == sorted(new_projects_soap, key=lambda x: x.name)

def random_string( maxlen): # функция генерирующая случайные строки
    symbols=string.ascii_uppercase + string.ascii_lowercase + string.digits #+ ""*10 #+ string.punctuation
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) # сгенерирована случайная длина символов не привышающая максимальную
