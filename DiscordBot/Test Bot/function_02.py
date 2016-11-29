# better way to get keys and values in Py3
def extraMessage(engine, **kwargs):
    if not kwargs:
        print(engine)

    else:
        if engine == 'youtube':
            search_engine = 'https://www.youtube.com/watch?v='
            print(search_engine)

            # for item in kwargs.items():
        for key, value in kwargs.items():
            variable_name = key
            print(variable_name)

            variable_value = value
            print(variable_value)


extraMessage(engine='youtube', name='ysPBhBfdUa5', nothing='hehe')
