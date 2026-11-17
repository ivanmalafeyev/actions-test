from collections.abc import Callable
from functools import wraps


def pname(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print(func.__name__)

    return wrapper


def deco(func: Callable) -> Callable:
    @wraps(func)
    def wrapper():
        import time

        start = time.time()

        func()
        end = time.time()
        print(f"Eval time = {(end - start):.5f}")

    return wrapper


@pname
@deco
def my_func():
    print("hi")


my_func()


def deco_pipe_params(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        from time import sleep

        sleep(1)
        func(*args, **kwargs)

    return wrapper


# @deco
@pname
@deco_pipe_params
def calc(a, b):
    return a + b


calc(1, 3)


def deco_with_params(repeat):
    def wrapper(func: Callable):
        @wraps(func)
        def inner(*args, **kwargs):
            nonlocal repeat
            print("start")
            for _ in range(repeat):
                func(*args, **kwargs)
            print("finish")

        return inner

    return wrapper


@pname
@deco_with_params(2)
def mmult(a, b):
    print(f"{a*b=}")


mmult(2, 3)
