import sys


def default():
    # This is the default case
    print("Hello!")


def cat():
    print("Meow!")


def dog():
    print("Woof!")


if __name__ == "__main__":
    if sys.argv[1] == 'dog':
        dog()
    elif sys.argv[1] == 'cat':
        cat()
    else:
        default()
