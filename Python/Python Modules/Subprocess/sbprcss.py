import subprocess

# We use subprocess module to run external commands
subprocess.run("ls")

# If we want to also use some options og the command
subprocess.run("ls -l", shell=True)

# The same command can be written also
subprocess.run(["ls", "-l"])

# Capture the output in a variable
variable_1 = subprocess.run("ls -l", shell=True)
# This way the command is still ran and the variable is
# the subprocess object and sowing us a __repr__ methof
print(variable_1)
# Because variable_1 is a subprocess object then we have
# some method to work for
print(f"Command args: {variable_1.args}")

# We can see the return code ( 0 = no errors)
print(variable_1.returncode) 

# Capture the output be real this time
variable_1 = subprocess.run("ls -l", shell=True, capture_output=True)
# This way the resault is saved as bytes so we have to convert into a string
print(variable_1.stdout.decode())

# The same lines of code can be written
variable_1 = subprocess.run("ls -l", shell=True, capture_output=True, text=True)
print(variable_1.stdout)

# What if we have an error
v = subprocess.run("ls -l dne", shell=True, capture_output=True, text=True)
# We are not getting any signal that we ahve done something bad
# We can check that with returncode method
print(v.returncode)
# Showing the error
print(v.stderr)

# But we can tell python that we want to see the error message
# v = subprocess.run("ls -l dne", shell=True, capture_output=True, text=True, check=True)

# Another example to test the input
try:
    v = subprocess.run("cat test.txt", shell=True, capture_output=True, text=True)
    search = subprocess.run("grep -n file", shell=True, capture_output=True, text=True, input=v.stdout)
    # grep [option] [word] [file], -n is for showing lines
    print(search.stdout)
except:
    pass