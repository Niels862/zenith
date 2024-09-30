#ifndef CODEX_DEFS_H
#define CODEX_DEFS_H

#include <stdint.h>

#define CODEX_UTF8_1B_HEADER 0x0
#define CODEX_UTF8_1B_START 7

#define CODEX_UTF8_2B_HEADER 0x6
#define CODEX_UTF8_2B_START 5

#define CODEX_UTF8_3B_HEADER 0xE
#define CODEX_UTF8_3B_START 4

#define CODEX_UTF8_4B_HEADER 0x1E
#define CODEX_UTF8_4B_START 3
#define CODEX_UTF8_4B_MAX 0x10FFFF

#define CODEX_UTF8_CONT_HEADER 0x2
#define CODEX_UTF8_CONT_START 6

#define CODEX_ERROR 0x80000000

#define CODEX_MASK(m) ((1 << (m)) - 1)

#define CODEX_APPEND(i, s, a) (((i) << (s)) | ((a) & CODEX_MASK(s)))

#define CODEX_MATCHES(i, s, h) ((((i) >> (s)) & CODEX_MASK(8 - (i))) == (h))

typedef uint32_t codex_codepoint_t;

#endif
