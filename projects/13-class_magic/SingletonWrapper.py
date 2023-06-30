# original source:
# https://github.com/Kemaweyan/singleton_decorator/blob/master/singleton_decorator/decorator.py

class _SingletonWrapper:
    def __init__(self, cls):
        self.__wrapped__ = cls
        self._instance = None

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = self.__wrapped__(*args, **kwargs)
        return self._instance


def singleton(cls):
    return _SingletonWrapper(cls)


@singleton
class Solo:
    def do_stuff(self):
        print("Stuff done by", hex(id(self)))


def main():
    instance = Solo()
    instance.do_stuff()
    Solo().do_stuff()
    print(instance)
    print(Solo())
    print(Solo)

if __name__ == '__main__':
    main()