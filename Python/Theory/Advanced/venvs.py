"""
Virtual Environments `solve` a very common `problem` that we might come across: 
    In our machine we run 2 (or more) scripts that need the same package, but let's
    say that the first script need an outdated version.

By default Python only `allows` us to have only 1 verison of a package.

In fact we can have only 1 version of a package in 1 `virtual environment`. But we can
have as `many` envs we want.

First of all to achive the `greatness` of `virtual enviroments` we need to install:
    'pip install virtualenv'

To `create` a virtual environment, we need a folder to capture all the packages we want,
let's say this folder is 'MyEnv'

We can `create` an env using (inside MyEnv folder):
    'python -m venv name'

(where name is the name of the virtual environment)

After that we need to `activate` the env using (inside MyEnv/name/Scripts folder):
    'activate'

To `in activate` the environment we use (inside MyEnv/name/Scripts folder):
    'deactivate'

To `delete` a virtual environment we use (inside MyEnv folder):
    'rmdir /s name'

    
The `convesion` is that each `application` of ours will has its own folder and also
its own `virtual environment`.
"""
