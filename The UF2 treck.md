## Links
Javascript library for compiling to uf2: https://www.npmjs.com/package/uf2
format specifications: https://microsoft.github.io/uf2/
Get info about uf2 files: https://microsoft.github.io/uf2/patcher/
History and info: https://makecode.com/blog/one-chip-to-flash-them-all
Language features present in typescript subset visible in uf2: https://makecode.com/language

**WHAT IS THIS**: https://github.com/microsoft/uf2/blob/master/utils/uf2conv.md

## Possibilities
- We have to write something that compiles code into uf2
- The device adds config data into the uf2 file
- HEX code gets parsed and dumped into the uf2 file via splitting it into chunks and adding metadata
- Something I've never heard of before called a 'HEX record' needs to get parsed and dumped into a uf2 file (see [here](https://en.wikipedia.org/wiki/Intel_HEX))
