import re
import quopri

class SignupHelper:

    def __init__(self, app):
        self.app = app

    def new_user(self, username, password, email):
        wd = self.app.wd
        wd.get(self.app.base_url + "/signup_page.php")
        wd.find_element_by_name("username").send_keys(username)
        wd.find_element_by_name("email").send_keys(email)
        wd.find_element_by_css_selector('input[type="submit"]').click()

        mail = self.app.mail.get_mail(username, password,"[MantisBT] Konto registrierung")
        url = self.extract_confirmation_url(quopri.decodestring(mail).decode()) # извлекаем ссылку для подтверждения из письма

        wd.get(url)
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_name("password_confirm").send_keys(password)
        wd.find_element_by_css_selector('input[value="Update User"]').click()

    def extract_confirmation_url(self, text):
        return re.search("http://.*$", text, re.MULTILINE).group(0) # в текте письма ищем ссылку начинающуюся с http:// и до конца строки .*$



