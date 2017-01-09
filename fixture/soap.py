from suds.client import Client
from suds import WebFault

class SoapHelper:
    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client()
        try:
            client.service.mc_login(username, password)
        except WebFault:
            return False



