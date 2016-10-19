# mkdir-p
Python 2 and 3 compatible POSIX mkdir -p.

## Introduction
POSIX `mkdir -p` command can create a directory recursively like Python's `os.makedirs`, but `mkdir -p` doesn't raise any error when the directory exists.
Therefore, the `mkdir_p` function in this package just use Python's `os.makedirs` and catch the error when the directory exists:
```python
from mkdir_p import mkdir_p
mkdir_p("path/to/the/dir/")
```
I totally don't know why I can't find some package doing this, but I found many implementations while searching it.
I don't know the original author who implement the version I refer to, so thanks to all of the answers on the internet.

## Installation
```
pip install mkdir-p
```
