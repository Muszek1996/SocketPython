import socket, pickle
import sys
from consolemenu import *
from consolemenu.items import *
import task
import priority

import time

host = 'localhost'
port = 50000
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))


def func():
    print("")


def getTasks():
    s.send("")


def addTask():
    opis = input("Opis zadania")
    submenu.start(False)
    submenu.join()
    priorytet = submenu.selected_option + 1

    newTask = task.Task(int(time.time() * 100), opis, priority.Priority(priorytet))
    databytes = pickle.dumps(newTask)
    s.send(databytes)


menu = ConsoleMenu("ToDo App")
function_item1 = FunctionItem("Dodaj zadanie", addTask)
function_item2 = FunctionItem("Wyswietl liste zadan", func)
function_item3 = FunctionItem("Usun zadanie", input, ["Podaj id zadania do usuniecia"])
submenu = ConsoleMenu("Wybierz Priorytet")
submenu_item1 = FunctionItem("Niski", func, None, None, None, True)
submenu_item2 = FunctionItem("Sredni", func, None, None, None, True)
submenu_item3 = FunctionItem("Wysoki", func, None, None, None, True)
submenu_item = SubmenuItem("Wyswietl zadania z okreslonym priorytetem", submenu, menu)
submenu.append_item(submenu_item1)
submenu.append_item(submenu_item2)
submenu.append_item(submenu_item3)

menu.append_item(function_item1)
menu.append_item(function_item2)
menu.append_item(function_item3)
menu.append_item(submenu_item)
menu.show()

while 1:
    msg = input("\nSend to server:")
    s.send(msg.encode())

    data = s.recv(size)
    sys.stdout.write("msg from server:" + data.decode())
s.close()
