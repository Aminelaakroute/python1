from datetime import datetime
import time


def Decorator(func):
    def wrapper():
        print("-" * 50)
        print(">Execution started {}".format(datetime.today().strftime("%Y-%m-%d %H:%M:%S")))
        func()
        print(">Execution Completed {}".format(datetime.today().strftime("%Y-%m-%d %H:%M:%S")))

    return wrapper


@Decorator
def Info_1():
    print("Hello World !!")
    time.sleep(2)
    print("How are you !!")


@Decorator
def Info_2():
    print("Bonjour le monde !!")
    time.sleep(2)
    print("Comment vas-tu !!")


@Decorator
def Info_3():
    print("Hola Mundo !!")
    time.sleep(2)
    print("Cómo estás !!")


Info_1()
Info_2()
Info_3()

print("-" * 50)
