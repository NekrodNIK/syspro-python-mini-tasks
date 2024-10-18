def specialize(func, *args, **kwargs):
    def wrapper(*f_args, **f_kwargs):
        return func(*args, *f_args, **kwargs, **f_kwargs)

    return wrapper
