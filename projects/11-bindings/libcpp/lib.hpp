namespace Foo {
    void func();
}

void func();
void func(int x);

extern "C" {
    void func_unmangled();
}
