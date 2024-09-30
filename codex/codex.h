#ifndef CODEX_H
#define CODEX_H

#include "defs.h"
#include <stddef.h>
#include <stdbool.h>

codex_codepoint_t codex_decode_utf8(char const *str, size_t *size);

#endif
