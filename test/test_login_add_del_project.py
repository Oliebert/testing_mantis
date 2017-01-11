from model.project import Project
import random
import string



def test_login(app):
    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")

def test_add_project(app):

    old_projects = app.project.get_projects_list()
    project = Project(name=random_string(5), description=random_string(10))
    app.project.create_project(project)
    new_projects = app.project.get_projects_list()
    old_projects.append(project)
    assert sorted(old_projects, key=lambda x: x.name) == sorted(new_projects, key=lambda x: x.name)


def test_del_project(app):
    if len(app.project.get_projects_list()) == 0:
        app.project.create_project(Project(name=random_string(5), description=random_string(10)))
    old_projects = app.project.get_projects_list()
    project = random.choice(old_projects)
    app.project.delete_project(project.name)
    new_projects = app.project.get_projects_list()
    old_projects.remove(project)
    assert sorted(old_projects, key=lambda x: x.name) == sorted(new_projects, key=lambda x: x.name)

def random_string( maxlen): # функция генерирующая случайные строки
    symbols=string.ascii_uppercase + string.ascii_lowercase + string.digits #+ ""*10 #+ string.punctuation
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) # сгенерирована случайная длина символов не привышающая максимальную



