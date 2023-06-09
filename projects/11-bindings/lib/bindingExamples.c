/* Example library code.
 * Compile and link with
 *      gcc -std=c17 -Wall -Wextra -Wpedantic -shared -fPIC bindingExamples.c -o libbindingExamples.so
 */

// ========================================================================== //

#include <stdio.h>
#include "bindingExamples.h"

// ========================================================================== //

const double pi = 3.14159265359;

// ========================================================================== //

void func_void_empty() {
    printf("called %s\n", __func__);
}

void func_void_int(int i) {
    printf("called %s with argument %d\n", __func__, i);
}

void func_void_charPtr(char* str) {
    printf("called %s with argument %s\n", __func__, str);
}

void func_void_doublePtr(const double* array) {
    printf("called %s with array. First element: %lf\n", __func__, *array);
}

void func_void_struct(point2d_t p) {
    printf("called %s with argument (%lf, %lf)\n", __func__, p.x, p.y);
}

void func_void_structPtr(point2d_t* p) {
    printf("called %s with argument (%lf, %lf)\n", __func__, p->x, p->y);
}

// ========================================================================== //

int func_int_empty() {
    printf("called %s\n", __func__);
    int result = 0;
    printf("  returning %d\n", result);
    return result;
}

/* Note: Never do this in real life.
 * The below code returns a pointer to a local variable, which should be free'd
 * after the call. In this case, it is a pointer to a part of the code segment
 * in which the constant "foo bar" is stored, so the lifetime of result actually
 * surpasses the function call.
 * But: There's no guarantee that the calling end respects the const.
 * You could end up with an attempted write access to the code segment, which
 * gives a segfault.
 */
const char* func_charPtr_empty() {
    printf("called %s\n", __func__);
    const char* result = "foo bar";
    printf("  returning \"%s\"\n", result);
    return result;
}
