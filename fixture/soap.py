from suds.client import Client
from suds import WebFault
from fixture.project import Project


class SoapHelper:
    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://mantis.stqa.ru/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
        except WebFault:
            return False

    def get_list_of_projects(self):
        client = Client("http://mantis.stqa.ru/api/soap/mantisconnect.php?wsdl")
        projects = client.service.mc_projects_get_user_accessible("administrator", "root")
        #Get the list of projects that are accessible to the logged in user.
        project_list = []
        for project in projects:
            name = project.name
            description = project.description
            project_list.append(Project(name=name, description=description))
        return project_list





'''class SoapFixture:
    def __init__(self, app):
        self.username = username
        self.password = password
        self.client = Client("http://mantis.stqa.ru/api/soap/mantisconnect.php?wsdl")


    def can_login(self, username, password):
        client = Client("http://mantis.stqa.ru/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
        except WebFault:
            return False
'''


