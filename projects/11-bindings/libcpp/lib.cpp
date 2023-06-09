/* Compile with:
 *   g++ -std=c++20 -Wall -Wextra -Wpedantic -fPIC -c lib.cpp
 * Link with
 *   g++ lib.o -shared -o libCpp.so
 */

#include <iostream>

#define WHOAMI() std::cout << __PRETTY_FUNCTION__ << std::endl

namespace Foo {
    void func() {WHOAMI();}
}

void func() {WHOAMI();}

void func([[maybe_unused]] int x) {WHOAMI();}

extern "C" {
    void func_unmangled() {WHOAMI();}
}
