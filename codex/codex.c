#include "codex.h"
#include <stdio.h>

codex_codepoint_t codex_decode_utf8(char const *str, size_t *size) {    
    if (str == NULL || size == NULL) {
        return 0;
    }

    char c = str[0];

    if (CODEX_MATCHES(c, CODEX_UTF8_1B_START, CODEX_UTF8_1B_HEADER)) {
        *size = 1;
        return c & CODEX_MASK(CODEX_UTF8_1B_START);
    }
    
    codex_codepoint_t dec;

    if (CODEX_MATCHES(c, CODEX_UTF8_2B_START, CODEX_UTF8_2B_HEADER)) {
        *size = 2;
        dec = c & CODEX_MASK(CODEX_UTF8_2B_START);
    } else if (CODEX_MATCHES(c, CODEX_UTF8_3B_START, CODEX_UTF8_3B_HEADER)) {
        *size = 3;
        dec = c & CODEX_MASK(CODEX_UTF8_3B_START);
    } else if (CODEX_MATCHES(c, CODEX_UTF8_4B_START, CODEX_UTF8_4B_HEADER)) {
        *size = 4;
        dec = c & CODEX_MASK(CODEX_UTF8_4B_START);
    } else {
        *size = 0;
        return CODEX_ERROR;
    }

    for (size_t i = 1; i < *size; i++) {
        c = str[i];

        if (CODEX_MATCHES(c, CODEX_UTF8_CONT_START, CODEX_UTF8_CONT_HEADER)) {
            dec = CODEX_APPEND(dec, CODEX_UTF8_CONT_START, c);
        } else {
            *size = 0;
            return CODEX_ERROR;
        }
    }

    if (dec > CODEX_UTF8_4B_MAX) {
        *size = 0;
        return CODEX_ERROR;
    }

    return dec;
}
