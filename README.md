# Word Counter

This utility will count the number of words in a file provided on the command-line. The 10 most common words and their occurrences will be displayed. It can be run via the command-line or included in a project as a library component. 

In module form, the utility will also parse a string. 


## Assumptions

A word is defined as a non-zero-length sequence of characters delimited by white space. Numbers also count as words although I debated including them. Entering no arguments will output the usage info.

## Prerequisites

To run this tool you need python3

### Usage

```
usage: word_counter.py [-h] [-f F]

optional arguments:
  -h, --help  show this help message and exit
  -f F        file to parse
```

### Samples

There are 3 sample files which can be run to verify the tool

```
python3 word_counter.py -f samples/dracula.txt
python3 word_counter.py -f samples/mobydick.txt
```


## Running the tests

```
python3 tests.py
```


