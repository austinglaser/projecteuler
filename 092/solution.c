/**@file    solution.c
 * @author  Austin Glaser <austin@boulderes.com>
 * @brief   Solution Source
 *
 * @addtogroup SOLUTION
 * @{
 *
 * @defgroup SOLUTION_PRIVATE Solution Private Members
 * @{
 */

/* --- PRIVATE DEPENDENCIES ------------------------------------------------ */

#include <assert.h>
#include <inttypes.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

/* --- PRIVATE CONSTANTS --------------------------------------------------- */

#define N UINT64_C(100)

_Static_assert(N >= 89, "N must be at leat 89 initially");

/* --- PRIVATE DATATYPES --------------------------------------------------- */

struct node {
    struct node *  next;
    struct node *  prev;
    bool           ends_in_cycle;
    uint64_t       value;
};

typedef struct node * node;

struct node_array {
    size_t  size;
    node    nodes[0];
};

typedef struct node_array * node_array;

/* --- PRIVATE MACROS ------------------------------------------------------ */
/* --- PRIVATE FUNCTION PROTOTYPES ----------------------------------------- */

static node node_create(uint64_t value);

static void node_destroy(node n);

static node_array node_array_create(size_t size);

static void node_array_resize(node_array * na, size_t new_size);

static node node_array_get(node_array * na, uint32_t i);

static void node_array_destroy(node_array na);

static uint64_t sum_squared_digits(uint64_t value);

/* --- PUBLIC VARIABLES ---------------------------------------------------- */
/* --- PRIVATE VARIABLES --------------------------------------------------- */
/* --- PUBLIC FUNCTIONS ---------------------------------------------------- */

int main(void)
{
    node_array na = node_array_create(N);
    if (na == NULL) {
        fprintf(stderr, "Could not create array\n");
        return -1;
    }

    node eighty_nine = node_array_get(&na, 89);
    node one         = node_array_get(&na, 1);

    eighty_nine->ends_in_cycle = true;

    eighty_nine->next = node_array_get(&na, sum_squared_digits(89));
    one->next = one;

    for (uint32_t n = 1; n <= N; n++) {
        node base = node_array_get(&na, n);
        node curr = base;

        /* Build chain forwards */
        while (!curr->ends_in_cycle && curr->value != 1) {
            uint64_t next_value = sum_squared_digits(curr->value);

            node next = node_array_get(&na, next_value);

            curr->next = next;
            next->prev = curr;

            curr = next;
        }
        node end = curr;

        /* Mark backwards */
        curr = end->prev;
        while (curr != NULL) {
            curr->ends_in_cycle = end->ends_in_cycle;
            node prev = curr->prev;
            curr->prev = NULL;
            curr = prev;
        }

    }

    printf("strict digraph {\n");

    for (uint32_t i = 0; i < na->size; i++) {
        if (na->nodes[i] != NULL) {
            node n = na->nodes[i];
            printf("\"%"PRIu64"\"", n->value);

            if (n->next != NULL) {
                printf(" -> \"%"PRIu64"\"", n->next->value);
            }

            printf(";\n");
        }
    }

    printf("}\n");

    node_array_destroy(na);
    return 0;
}

/* --- PRIVATE FUNCTION DEFINITIONS ---------------------------------------- */

static node node_create(uint64_t value)
{
    node n = malloc(sizeof(*n));
    if (n == NULL) {
        fprintf(stderr, "%s: memory allocation failed\n", __func__);
        return NULL;
    }

    n->next          = NULL;
    n->prev          = NULL;
    n->ends_in_cycle = false;
    n->value         = value;

    return n;
}

static void node_destroy(node n)
{
    if (n) free(n);
}

static node_array node_array_create(size_t size)
{
    node_array na = malloc(sizeof(*na) + size * sizeof(na->nodes[0]));
    if (na == NULL) {
        fprintf(stderr, "%s: memory allocation failed\n", __func__);
        return NULL;
    }

    na->size = size;

    for (uint32_t i = 0; i < size; i++) {
        na->nodes[i] = NULL;
    }

    return na;
}

static void node_array_resize(node_array * na, size_t new_size)
{
    node_array new_na = realloc(*na, sizeof(**na) + new_size * sizeof((*na)->nodes[0]));
    if (new_na == NULL) {
        fprintf(stderr, "%s: memory allocation failed\n", __func__);
        node_array_destroy(*na);
        exit(1);
    }

    *na = new_na;

    for (uint32_t i = (*na)->size; i < new_size; i++) {
        (*na)->nodes[i] = NULL;
    }

    (*na)->size = new_size;
}

static node node_array_get(node_array * na, uint32_t i)
{
    if (i == 0) {
        return NULL;
    }

    if (i > (*na)->size) {
        node_array_resize(na, i);
    }

    if ((*na)->nodes[i-1] == NULL) {
        (*na)->nodes[i-1] = node_create(i);
    }

    return (*na)->nodes[i-1];
}

static void node_array_destroy(node_array na)
{
    if (na) {
        for (uint32_t i = 0; i < na->size; i++) {
            node_destroy(na->nodes[i]);
        }
        free(na);
    }
}

static uint64_t sum_squared_digits(uint64_t value)
{
    uint64_t sum = 0;
    while (value != 0) {
        uint32_t digit = value % 10;
        sum += digit*digit;
        value /= 10;
    }

    return sum;
}

/** @} defgroup SOLUTION_PRIVATE */
/** @} addtogroup SOLUTION */
