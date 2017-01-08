from selenium import webdriver    #.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper
from fixture.james import JamesHelper
from fixture.signup import SignupHelper
from fixture.mail import MailHelper

class Application:

    def __init__(self, browser, config):

        if browser == "firefox":
            self.wd = webdriver.Firefox()#firefox_binary="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s " % browser)

        self.session = SessionHelper(self)

        self.project = ProjectHelper(self)

        self.james = JamesHelper(self)

        self.config = config

        self.base_url = config["web"]["baseUrl"]
                                                    #driver wird ein einziges Mal inizilisiert bei der Erschaffung einer Fixture.
                                                    #ein Helper übernimmt einen Link auf ein Objekt der Klasse Application
                                                    #was uns die Möglichkeit gibt über einen Helper uns zu anderem wenden
        self.signup= SignupHelper(self)

        self.mail = MailHelper(self)


    def is_valid(self):
        try:
            self.wd.current_url                     #URL of the current loaded page
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)


    def destroy(self):
        self.wd.quit()