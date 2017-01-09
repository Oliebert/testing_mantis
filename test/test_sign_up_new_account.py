import string
import random

def random_string(prefix, maxlen): # функция генерирующая случайные строки
    symbols = string.ascii_letters#symbols=string.ascii_uppercase + string.ascii_lowercase + string.digits #+ ""*10 #+ string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) # сгенерирована случайная длина символов не привышающая максимальную

def test_sign_up_new_account(app):
    username =random_string("user__", 10)
    email = username + "@localhost"
    password ="test"
    app.james.ensure_user_exists(username, password)
    app.signup.new_user(username, password, email)
    app.session.login(username, password)
    assert app.session.is_logged_in_as(username)
    app.session.logout()