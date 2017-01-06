import pytest
from fixture.application import Application
import jsonpickle
import os.path
import importlib
import json
#from fixture.db import DbFixture


fixture = None                                                                                   #фикстура не определена
target = None

def load_config(file): # функция загрузки конфигурации target
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file) # получаем информацию о пути к текущему файлу
        with open(config_file) as f:  # затем пришиваем к ней target
            target = json.load(f)
    return target

@pytest.fixture
def app(request):

    global fixture

    browser = request.config.getoption("--browser")                   # получаем доступ к сохраненному параметру browser
    web_config = load_config(request.config.getoption("--target"))['web']

    if fixture is None or not fixture.is_valid():                                   # случай если фикстура не определена
        fixture = Application(browser=browser, base_url=web_config['baseUrl'])                              # или не валидна
 #   fixture.session.ensure_login(username=web_config['username'], password=web_config['password'])
    return fixture

@pytest.fixture
def check_ui(request):
    return request.config.getoption("--check_ui")


'''
@pytest.fixture(scope="session") # фикстура для загрузки базы данных
def db(request):
    db_config = load_config(request.config.getoption("--target"))['db']
    dbfixture = DbFixture(host= db_config['host'], name = db_config['name'], user = db_config['user'], password = db_config['password'])

    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture
'''

@pytest.fixture(scope="session", autouse=True)                                      # фикстура выполняется автоматически
def stop(request):

    def fin():

        fixture.session.ensure_logout()                                            # убеждаемся что мы вывшли из системы
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser): #parser нам нужен для того чтобы код из командной строки понимался в Питоне

    parser.addoption("--browser", action="store", default="firefox")  # действие - сохранить значение параметра browser
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--check_ui", action="store_true")

def pytest_generate_tests(metafunc): # параметр metafunc содержит информацию о вызываемом методе, для которого генерируются данные
                                     #в частности, он содержит информацию о фикстурах, которые требуются этому методу
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:]) # загружаем тестовые данные из модуля, который имеет такое же название как фикстура только обрезанное
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])

        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])  # загружаем тестовые данные из документа json, который имеет такое же название как фикстура только обрезанное
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])

def load_from_json(file):
    with open (os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())


def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata # или ('.' + <имя модуля>, имя данных)
