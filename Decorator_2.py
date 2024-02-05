from datetime import datetime
import time


def Decorator(func):
    def wrapper(*args, **kwargs):
        print("-" * 50)
        print(">Execution started {}".format(datetime.today().strftime("%Y-%m-%d %H:%M:%S")))
        func(*args, **kwargs)
        print(">Execution started {}".format(datetime.today().strftime("%Y-%m-%d %H:%M:%S")))
        print("-" * 50)

    return wrapper


@Decorator
def function_args(sleep_time):
    print("Executing task!")
    time.sleep(sleep_time)
    print("Task complete!")


function_args(1)
function_args(2)
function_args(3)