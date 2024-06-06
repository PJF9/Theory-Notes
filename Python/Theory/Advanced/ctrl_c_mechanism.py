
def ctrl_c_exit(funct):
    def wrapper(*args, **kwargs):
        rv = None
        try:
            rv = funct(*args, **kwargs)
        except KeyboardInterrupt:
            print()
            print(" Rage quit...")

        return rv
    return wrapper


@ctrl_c_exit
def main():

    i: int = 0
    while True:
        print(i)
        i += 1

main()
