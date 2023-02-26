def showcase_object_locality():
    print("### IN SHOWCASE_OBJECT_LOCALITY")
    x = 2
    print("globals:", globals())
    print("locals :", locals())
    print("globals and locals are", "same" if globals() == locals() else "different")
    print("x =", x)
    print("x_globals = ", globals()['x'])
    print("x_locals  = ", locals()['x'])


def read_access_global():
    print("### IN READ_ACCESS_GLOBAL")
    print(x)  # x = 2 -- forbidden, as x is already bound to the object in globals()


def read_write_access_global():
    print("### IN READ_WRITE_ACCESS_GLOBAL")
    global x
    print(x)
    x = 2  # now allowed due to explicit binding to the object in globals


def mutating_read_access(data):
    print("### IN MUTATING_READ_ACCESS")
    data.append(1)
    print("data =", data)
    print("id(data) =", id(data))
    print("local data and global array are", "" if locals()['data'] is globals()['array'] else "not", "the same")
    data = [2]
    print("after overwriting:")
    print("id(data) =", id(data))
    print("local data and global array are", "" if locals()['data'] is globals()['array'] else "not", "the same")


if __name__ == '__main__':
    print("### AT MAIN")
    print("globals:", globals())
    print("locals :", locals())
    print("globals and locals are", "same" if globals() == locals() else "different")

    x = 1
    print("x =", x)
    print("x_globals = ", globals()['x'])
    print("x_locals  = ", locals()['x'])

    showcase_object_locality()
    read_access_global()
    read_write_access_global()

    print("### AT MAIN")
    print(x)

    y = x
    print("y = ", y)
    print("y is", "" if y is x else "not", "x")
    del x

    print("globals does", "" if 'x' in globals() else "not", "contain x")
    # print(x) -- will give a NameError -- x does no longer exist
    # read_access_global() -- same
    # showcase_object_locality() -- will give a KeyError when trying to access globals['x']
    print("y:", y)  # y and the referred to object still exist
    # print("y is", "" if y is x else "not", "x") -- again, NameError

    array = []
    print("array =", array)
    print("id(array) = ", id(array))
    mutating_read_access(array)
    print("### AT MAIN")
    print(array)

    globals()['z'] = 1
    print(z)
