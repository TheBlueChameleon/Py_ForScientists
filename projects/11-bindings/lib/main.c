/* Example code using.
 * Compile and link with
 *      gcc -std=c17 -Wall -Wextra -Wpedantic main.c -lbindingExamples -L. -Wl,-rpath=. -o sharedLibraryTest
 */

#include "bindingExamples.h"

int main () {
    point2d_t p = {-1, pi};

    func_void_empty();
    func_void_int(-1);
    func_void_charPtr("foo bar");
    func_void_doublePtr(&pi);
    func_void_struct(p);
    func_void_structPtr(&p);

    func_int_empty();
    func_charPtr_empty();
}
