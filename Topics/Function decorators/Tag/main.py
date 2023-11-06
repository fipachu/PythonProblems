def tagged(func):
    def wrapper(*args, **kwargs):
        func_result: str = func(*args, **kwargs)
        return f'<title>{func_result}</title>'
    return wrapper
