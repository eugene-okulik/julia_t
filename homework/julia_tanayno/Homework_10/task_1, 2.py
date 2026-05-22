# task_1


def finish_me(func):

    def wrapper(*args):
        result = func(*args)
        print("finished")
        return result
    return wrapper


@finish_me
def example(text):
    print(text)


example("print me1")


# task_2.1

def repeat_me(func):
    def wrapper(*args, **kwargs):
        count_1 = int(kwargs.get('count'))
        for i in range(count_1):
            func(*args)
    return wrapper


@repeat_me
def example(text):
    print(text)


example("print me2", count=2)

# task_2.2


def repeat_me(count):
    def decorator(func):
        def wrapper(*args):
            for i in range(count):
                func(*args)
        return wrapper
    return decorator


@repeat_me(count=2)
def example(text):
    print(text)


example("print me3")
