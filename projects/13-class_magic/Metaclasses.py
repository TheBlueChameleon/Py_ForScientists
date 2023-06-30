def construct_classes_manually():
    A = type('A', (), {'attribute': 0})
    B = type('The class B', (A,), {})

    a = A()
    b = B()

    print(f"{type(A)=}")
    print(f"{type(a)=}")
    print(f"{type(B)=}")
    print(f"{type(b)=}")
    print(f"{b.__class__=}")
    print()

    print(f"{b.attribute=}")
    print(f"{isinstance(b, A)=}")
    print(f"{issubclass(B, A)=}")

def foo():
    class SingletonMeta(type):
        def _new(cls, *args, **kwargs):
            if cls._instance is None:
                cls._instance = super(cls, cls).__new__(cls, *args, **kwargs)
            return cls._instance

        def __init__(cls, name, bases, members):
            cls._instance = None
            cls.__new__ = SingletonMeta._new

    Cls = SingletonMeta('Cls', (), {})
    inst_1 = Cls()
    inst_2 = Cls()
    print(Cls)
    print(dir(Cls))
    print()
    print(inst_1)
    print(dir(inst_1))
    print(inst_1 is inst_2)



def main():
    # construct_classes_manually()
    foo()

if __name__ == '__main__':
    main()