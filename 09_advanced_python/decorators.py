def log_call(function):
    def wrapper(*args, **kwargs):
        print(f"Calling {function.__name__}")
        result = function(*args, **kwargs)
        print(f"Returned {result}")
        return result
    return wrapper

@log_call
def add(a, b):
    return a + b

add(5, 7)
