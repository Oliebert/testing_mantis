import string
from model.project import Project
import random
import os.path
import sys
import getopt
import jsonpickle

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"]) # n - количество генерируемых данных,
except getopt.GetoptError as err:                                                 # f- файл в который это все помещается
    # sys.argv это список параметров, которые переданы в программу из командной строки при запуске
    #1: это диапазон от второго элемента списка до последнего
    #почему от второго? потому что первый элемент в sys.argv это сам запускаемый сценарий, а дальше уже идут опции

    getopt.usage()
    sys.exit(2)

n = 5
f = "data/projects_data.json"

for o, a in opts:                   # o - название опции, a - ее значение
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen): # функция генерирующая случайные строки
    symbols=string.ascii_letters + string.digits #+ " "*10 + string.punctuation
    return prefix + "".join ([random.choice(symbols) for i in range(random.randrange(maxlen))]) # сгенерирована случайная длина символов не привышающая максимальную

testdata = [Project(name="", status="", description="")] + [
            Project(name=random_string("name", 10), status=random_string("status", 20), description=random_string("description", 50))
             for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f )

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))