def filter_first_key(filter_key):
    def f(func):
        def wrapper(*args, **kwargs):
            return func(
                {k: v for k, v in dict(args[0]).items()
                 if filter_key == '' or str(filter_key).lower() == str(k).lower()}, **kwargs
            )
        return wrapper
    return f


def time_result(func):
    def wrapper(*args, **kwargs):
        time_1 = time()
        f = func(*args, **kwargs)
        time_2 = time() - time_1
        return f, time_2
    return wrapper


@time_result
@filter_first_key('ivan')
def custom_filter(dictionary: dict, name_in='', year='99', key=''):
    return {
        k: dict(filter(lambda k: str(k[0]).lower() == key.lower() if key != '' else k, v.items()))
        for k, v in dictionary.items()
        if v.get("year") < int(year)
        if str(name_in).lower() in str(k).lower()
    }


if __name__ == '__main__':
    dictionary = {'ivan': {'year': 10, 'job': 'dev'}, 'bob': {'year': 20, 'city': 'Paris'}}
    print(custom_filter(dictionary, key='job'))
