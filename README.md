# Editing binaries - homework

## Contents
- Searching for a Bit Sequence in Input Files
- Searching and Replacing a Bit Sequence in Input Files

## This script allows for:
- Bit Sequence Search: Locate and display all occurrences of a specified bit sequence within a binary file.
- Bit Sequence Search and Replace: Locate a specified bit sequence within a binary file and replace it with another bit sequence, saving the modified data to a new file.
  

1. Search Mode (f): Finds and outputs all positions of a specified bit sequence within a binary file.
```
dn1 test.bin f 0100
```
- test.bin: Input binary file.
- f: Search mode.
- 0100: The bit sequence to search for


  
2. Search and Replace Mode (fr): Finds and replaces all occurrences of a specified bit sequence with a new bit sequence, saving the modified data to a new file.
```
dn1 test.bin fr 0100 0110
```
- test.bin: Input binary file.
- fr: Search and replace mode.
- 0100: Bit sequence to search for.
- 0110: Bit sequence to replace with.
