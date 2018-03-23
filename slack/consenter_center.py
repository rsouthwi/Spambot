

class PrintHook(object):
    def __init__(self, *args, **kwargs):
        print("args: {}".format(args))
        print("kwargs: {}".format(kwargs))
        

class NewLegaleseHook(object):
    pass


class CustomerConsentHook(object):
    pass


