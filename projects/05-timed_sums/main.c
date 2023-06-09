// gcc -std=c17 -Wall -Wextra -Wpedantic -mavx512f -O3 main.c && ./a.out

#include <stdio.h>
#include <time.h>
#include <immintrin.h>

// ========================================================================== //

void naive(int N) {
    printf("naive:\n");
    clock_t tic = clock();

    long long int sum = 0;
    for (int i = 0; i < N; ++i) {
        sum += i;
    }

    clock_t toc = clock();
    double delta_t = 1000.0 * (toc - tic) / CLOCKS_PER_SEC;
    printf("got %lld in %f ms\n", sum, delta_t);
}

// -------------------------------------------------------------------------- //

void intrinsics(int N) {
    printf("intrinsics:\n");
    clock_t tic = clock();

    __m512i accumulator = {0};
    __m512i summand = {0};
    long long int sum_intrinsics = 0;
    for (int i = 0; i < N; i+=8) {
        for (int j = 0; j < 8; ++j) {
            summand[j] = i + j;
        }

        accumulator = _mm512_add_epi64 (accumulator, summand);
    }

    for (int j = 0; j < 8; ++j) {
        sum_intrinsics += accumulator[j];
    }

    clock_t toc = clock();
    double delta_t = 1000.0 * (toc - tic) / CLOCKS_PER_SEC;
    printf("got %lld in %f ms\n", sum_intrinsics, delta_t);
}

// -------------------------------------------------------------------------- //

void intrinsics_improved(int N) {
    printf("intrinsics improved:\n");
    clock_t tic = clock();

    __m512i accumulator = {0};
    __m512i summand     = {0, 1, 2, 3, 4, 5, 6, 7};
    __m512i delta       = {8, 8, 8, 8, 8, 8, 8, 8};
    long long int sum_intrinsics = 0;
    for (int i = 0; i < N; i += 8) {
        accumulator = _mm512_add_epi64 (accumulator, summand);
        summand     = _mm512_add_epi64 (summand, delta);
    }

    for (int j = 0; j < 8; ++j) {
        sum_intrinsics += accumulator[j];
    }

    clock_t toc = clock();
    double delta_t = 1000.0 * (toc - tic) / CLOCKS_PER_SEC;
    printf("got %lld in %f ms\n", sum_intrinsics, delta_t);
}

// ========================================================================== //

int main () {
    const int N = 1E+6;

    naive(N);
    intrinsics(N);
    intrinsics_improved(N);
}
