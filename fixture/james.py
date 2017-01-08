from telnetlib import Telnet
class JamesHelper:

    def __init__(self, app):
        self.app = app

    def ensure_user_exists(self, username, password):
        james_config = self.app.config["james"]
        session = JamesHelper.Session(james_config["host"], james_config["port"], james_config["password"], james_config["username"])
        if session.is_users_registered(username):# если пользователь зарегистрирован, меняем пароль
            session.reset_password(username, password)
        else:
            session.create_user(username, password)

        session.quit()



    class Session:

        def __init__(self, host, port,username, password): # логин и пароль для доступа к почтовому серверу
            self.telnet = Telnet(host, port, 5) # если сервер не отвечает , ждем 5 сек
            self.read_until("Login id:")# выполняем вход с указанными именем пользователя и паролем,
            self.write(username + "\n")# вводим имя пользователя
            self.read_until("Password:")
            self.write(password + "\n")  # вводим пароль
            self.read_until("Welcome root. HELP for a list of commands") # строка,появляющаяся после успешного входа в систему

        def read_until(self, text):
            self.telnet.read_until(text.encode("ascii"), 5) #читаем до тех пор пока не встретится текст перекодированый в набор байтов

        def write(self, text):
            self.telnet.write(text.encode("ascii"))

        def is_users_registered(self, username):
            self.write("verify %s\n" % username)
            res = self.telnet.expect([b"does not exist", b"exist", ])
            return res[0] == 1 # if "does not exist" - True

        def create_user(self, username, password):
            self.write("adduser %s %s\n"% (username, password))
            self.read_until("User %s added" % username) #строку, являющуюся результатом подстановки,
                                                                  #перекодировать в байтовую можно с помощью encode

        def reset_password(self,username, password ):
            self.write("setpassword %s %s\n" % (username, password))
            self.read_until("Password for %s reset" % username)

        def quit(self):
            self.write("quit\n")



