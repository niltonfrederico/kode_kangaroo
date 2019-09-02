def snakecase_dict(func):
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        if type(response) not in (dict, list):
            raise TypeError("Function return must be a dict or list of dicts.")

        return response

    return wrapper
