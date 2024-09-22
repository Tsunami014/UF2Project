## Links
Javascript library for compiling to uf2: https://www.npmjs.com/package/uf2
format specifications: https://microsoft.github.io/uf2/
Get info about uf2 files: https://microsoft.github.io/uf2/patcher/
History and info: https://makecode.com/blog/one-chip-to-flash-them-all
Language features present in typescript subset visible in uf2: https://makecode.com/language

**WHAT IS THIS**: https://github.com/microsoft/uf2/blob/master/utils/uf2conv.md

## Possibilities
- Maybe [these target things](https://github.com/microsoft/pxt/blob/1e22ec7a07a5979d06b050bff407741a6e987c08/docs/targets/pxtarget.md) are important?
- We have to write something that compiles code into uf2
- The device adds config data into the uf2 file
- HEX code gets parsed and dumped into the uf2 file via splitting it into chunks and adding metadata
- Something I've never heard of before called a 'HEX record' needs to get parsed and dumped into a uf2 file (see [here](https://en.wikipedia.org/wiki/Intel_HEX))
- WHAT IF we use the STM32 cube IDE to compile code and then convert that using the files we found into a uf2 file?
