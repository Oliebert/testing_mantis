'''
ein Class for login und logout session
'''

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd                       # Zugang zu Driver wird benötigt
        self.app.open_home_page()
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys(username)
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_css_selector('input[type="submit"]').click()


    def logout(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[@id='logout-link']").click()

    def ensure_logout(self):
            wd = self.app.wd
            if self.is_logged_in():
                self.logout()


    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return self.get_logger_user() == username

    def get_logger_user(self):
        wd = self.app.wd
        return wd.find_element_by_xpath("//span[@id='logged-in-user']").text
        #return len(wd.find_elements_by_xpath("//div/div[1]/form/b[.='(%s)']" % username)) #(wd.find_element_by_xpath("//div/div[1]/form/b").text=="("+username+")")


    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)
        if not self.is_logged_in():
            raise ValueError ("password or name is false")