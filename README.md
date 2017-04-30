## justdb

[![Build Status](https://travis-ci.org/kootenpv/justdb.svg?branch=master)](https://travis-ci.org/kootenpv/justdb)
[![Coverage Status](https://coveralls.io/repos/github/kootenpv/justdb/badge.svg?branch=master)](https://coveralls.io/github/kootenpv/justdb?branch=master)
[![PyPI](https://img.shields.io/pypi/v/justdb.svg?style=flat-square)](https://pypi.python.org/pypi/justdb/)
[![PyPI](https://img.shields.io/pypi/pyversions/justdb.svg?style=flat-square)](https://pypi.python.org/pypi/justdb/)

### Why

`justdb` is a thread/process safe, file-based database, without strain for the developer.

The interesting thing is that there will be a _detached_ process which
will receive requests through ZeroMQ. This process will ensure only 1
thread or process can write at a time. Even external processes.

The process will however not write data to files itself, it only communicates permission.
Like this, you can make it safe to write/read to a filesystem, and benefit from great speed.

For more capabilities, also read here: [just](https://github.com/kootenpv/just).

### Installation

    pip install justdb

## Using justdb

```python
from justdb import JustDB
j = JustDB()

# write to file (serialization based on filename)
j["bla.json"] = {"a": 1}

# read file (deserialization based on filename)
print(j["bla.json"])
# {"a": 1}

# remove file
j.remove("bla.json")

# also works with other extension **.
j["some/folder/bla.yml"] = {"a": 1}
print(j["some/folder/bla.yml"])
# {"a": 1}
```

** See [supported types](https://github.com/kootenpv/just/blob/master/just/__init__.py#L28).

### SPEED

Ok, `just` is rather slow. If you want to do fast writing without file extension and file existance checks:

```python
import ujson
def my_read():
    with open("some.json") as f:
        return ujson.load(f)
result = j.execute(my_read)
```

Like this, you will be faster than Redis.

### Stop the server

    justdb kill

### Warning

Note that whatever function you will use with `j.execute()` (or with `j` in general), you can be assured that it will be the only function running (well, using `JustDB`, if you write without justdb to the same files, good luck).

## root path

It will search for a `.just` file to consider as root, upwards.
