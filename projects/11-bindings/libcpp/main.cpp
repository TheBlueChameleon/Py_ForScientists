/* Compile and link with:
 *   g++ -std=c++20 -Wall -Wextra -Wpedantic    main.cpp -lCpp -L. -Wl,-rpath=. -o sharedLibraryTest
 */

#include "lib.hpp"

int main() {
    Foo::func();
    func();
    func(0);
    func_unmangled();
}
