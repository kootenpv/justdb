## justdb

[![Build Status](https://travis-ci.org/kootenpv/justdb.svg?branch=master)](https://travis-ci.org/kootenpv/justdb)
[![Coverage Status](https://coveralls.io/repos/github/kootenpv/justdb/badge.svg?branch=master)](https://coveralls.io/github/kootenpv/justdb?branch=master)
[![PyPI](https://img.shields.io/pypi/v/justdb.svg?style=flat-square)](https://pypi.python.org/pypi/justdb/)
[![PyPI](https://img.shields.io/pypi/pyversions/justdb.svg?style=flat-square)](https://pypi.python.org/pypi/justdb/)

### Why

It is thread/process safe, without strain for the developer.

Also, to find more capabilities, read about [just](https://github.com/kootenpv/just).

### Installation

pip install justdb

## Using justdb

```python
j = JustDB()
j["some/folder/bla.json"] = {"a": 1}
print(j["some/folder/bla.json"])
# {"a": 1}
```

It will create a folder

### SPEED

Ok, `just` is rather slow. If you want to do fast writing without file extension and file existance checks:

```python
import ujson
def my_read():
    with open("some.json") as f:
        return ujson.load(f)
result = j.execute(my_read)
```

Like this, you will be faster than Redis. Note that whatever function you will put here, you can be assured that it will be the only function running (well, using `JustDB`).

### Warning

Note that if you do writes/reads outside of using the JustDB, you can still get into race conditions.

## root path

It will search for a `.just` file to consider as root, upwards.
