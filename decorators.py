import time


def time_logger(func):
    def get_time_delta(*a, **kw):
        time_before = time.time()
        result = func(*a, **kw)
        time_after = time.time()
        print('Function is performed in {} ms'.format((time_after-time_before)*1000))
        return result
    return get_time_delta


@time_logger
def exp(n):
    return n**n


exp(100000)
