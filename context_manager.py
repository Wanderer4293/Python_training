class CustomContextManager:

    def __init__(self, func, args, kwargs):
        self.gen = func(*args, **kwargs)

    def __enter__(self):
        try:
            return next(self.gen)
        except StopIteration:
            raise RuntimeError('Generator didn\'t yield')

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            try:
                next(self.gen)
            except StopIteration:
                return False
        self.gen.throw(exc_type, exc_val, exc_tb)


def custom_context_manager(func):
    def wrapper(*args, **kwargs):
        return CustomContextManager(func, args, kwargs)
    return wrapper


@custom_context_manager
def open_file(path, rights):
    f = open(path, rights)
    try:
        yield f
    except Exception as e:
        raise e
    finally:
        f.close()


if __name__ == '__main__':
    with open_file('sample.txt', 'w') as file:
        file.write('Another')
