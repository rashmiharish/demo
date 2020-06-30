import sys


def default():
    # This is the default case
    print("Hello!")


def cat():
    print("Meow!")

if __name__ == "__main__":
    if sys.argv[1] == 'cat':
        cat()
    else:
        default()
