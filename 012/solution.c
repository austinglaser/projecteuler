/**
 * @file    solution.c
 * @author  Austin Glaser <austin@boulderes.com>
 * @brief   P12 Solution
 *
 * @addtogroup SOLUTION
 * @{
 */

/* --- PRIVATE DEPENDENCIES ------------------------------------------------- */

// Standard
#include <stdio.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

/* --- PRIVATE CONSTANTS ---------------------------------------------------- */
/* --- PRIVATE DATATYPES ---------------------------------------------------- */
/* --- PRIVATE MACROS ------------------------------------------------------- */
/* --- PRIVATE FUNCTION PROTOTYPES ------------------------------------------ */
/* --- PUBLIC VARIABLES ----------------------------------------------------- */
/* --- PRIVATE VARIABLES ---------------------------------------------------- */
/* --- PUBLIC FUNCTIONS ----------------------------------------------------- */

int compare_uint32_t(const void *v1p, const void *v2p) {
    const uint32_t v1 = *((const uint32_t *) v1p);
    const uint32_t v2 = *((const uint32_t *) v2p);

    return (v1 > v2) - (v1 < v2);
}

int32_t prime_factors(uint32_t number, uint32_t *pf_arr, uint32_t pf_arr_len) {
    uint32_t max_divisor = (uint32_t) floor(sqrt(number));

    if (pf_arr_len <= 0) return -1;

    uint32_t d;
    for (d = max_divisor; d > 1; d--) {
        if (number % d == 0) {
            int32_t i = prime_factors(d, pf_arr, pf_arr_len);
            int32_t j = prime_factors(number/d, pf_arr + i, pf_arr_len - i);
            return (j > 0) ? i + j : -1;
        }
    }
    pf_arr[0] = number;
    return 1;
}

void print_array(uint32_t *arr, uint32_t len) {
    uint32_t i;
    printf("[");
    for (i = 0; i < len; i++) {
        printf("%u,", arr[i]);
    }
    printf("\b]");
}

uint32_t n_divisors(uint32_t number) {
    uint32_t pf_arr[2000];
    int32_t n = prime_factors(number, pf_arr, 2000);
    qsort(pf_arr, n, sizeof(uint32_t), compare_uint32_t);

    int32_t i;
    uint32_t current = pf_arr[0];
    uint32_t current_idx = 0;
    uint32_t totals[2000];
    memset(totals, 0, sizeof(totals));
    for (i = 0; i < n; i++) {
        if (pf_arr[i] != current) {
            current = pf_arr[i];
            current_idx++;
        }
        totals[current_idx]++;
    }
    int32_t n_totals = current_idx + 1;
    uint32_t product = 1;
    for (i = 0; i < n_totals; i++) {
        product *= (totals[i] + 1);
    }
    return product;
}

int main(void)
{
    uint32_t triangle = 0;
    uint32_t n = 1;

    while (n_divisors(triangle) < 500) {
        triangle += n;
        n++;
    }
    printf("%u\n", triangle);
}

/* --- PRIVATE FUNCTION DEFINITIONS ----------------------------------------- */

/** @} addtogroup SOLUTION */
