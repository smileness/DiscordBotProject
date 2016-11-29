def extraMessage(engine, **kwargs):
    if not kwargs:
        print(engine)

    else:
        if engine == 'youtube':
            search_engine = 'https://www.youtube.com/watch?v='
            print(search_engine)

        for item in kwargs.keys():
            if item == 'name':
                variable_name = item
                print(variable_name)

                variable_value = kwargs[item]
                print(variable_value)
            else:
                pass


extraMessage(engine='youtube', name='ysPBhBfdUa5', nothing='hehe')
