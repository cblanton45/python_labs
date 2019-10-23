## Fortran Plus Python

We have an example Fortran module here:

[Fortran Primes Code](./primes.f95)

It implments the sieve of Erososthenes to generate a sequence of prime numbers.  More about the sieve of Erosostenes here: 
[Sieve of Erososthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)


To compile:

```bash
f2py3 -c primes.f95 -m primes
```


This should generate a compiled library file.  The name of the file will depend on your platform, for example, on MacOS, the file will 
look something like this: `primes.cpython-37m-darwin.so`.

Now you can start you python or jupyter notebook. For example, you can start the python like this:

```bash
python
```

and you should get the console
```pycon
Python 3.7.3 (default, Mar 27 2019, 16:54:48)
[Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

You can also start jupyter notebook:

```bash
jupyter notebook
```

Which will bring up jupyter notebook with the folder containing the `.so` file mentioned above in the PWD.

Once you are up (either in the python console or in jupyter notebook, we should be able to run the following python code:

```pycon
>>> import primes
>>> sieve_array = primes.sieve(100)
>>> prime_numbers = primes.logical_to_array(sieve_array, sum(sieve_array))
>>> print(prime_numbers)
[ 2  3  5  7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97]
```

Note the output, as expected, is the sequence of prime numbers.


