# Test C Application

This is a test hello world C module.  All it does is print "hello"


## How to build
```bash
python setup.py build
```

Notice that there will be a new directory created called "build".  What appears in tha directory
will depend on your platform.  For example, on MacOS you will see somehting like this:

```console
# Mac
lib.macosx-10.6-x86_64-3.5/myModule.cpython-35m-darwin.so
temp.macosx-10.6-x86_64-3.5/test.o
```

On Linux, it will look like this.

```console
# Linux
./lib.linux-x86_64-3.6/myModule.cpython-36m-x86_64-linux-gnu.so
./temp.linux-x86_64-3.6/test.o
```

## How to Install

```bash
python setup.py install
```

```console
running install
running build
running build_ext
running install_lib
copying build/lib.macosx-10.6-x86_64-3.5/myModule.cpython-35m-darwin.so -> //anaconda/lib/python3.5/site-packages
running install_egg_info
Writing //anaconda/lib/python3.5/site-packages/myModule-1.0-py3.5.egg-info
```


## How to run
```bash
python hello.py
```

```console
Hello World
```

That code was called from C++! It worked!






