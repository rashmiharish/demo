import sys


def default():
    # This is the default case
    print("Hello!")


def dog():
    print("Woof!")


if __name__ == "__main__":
    if sys.argv[1] == 'dog':
        dog()
    else:
        default()
