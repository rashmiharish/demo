import sys


def default():
    # This is the default case
    print("Hello!")


def cat():
    print("Meow!")


def dog():
    print("Woof!")


def cow():
    print("Moo!")

def pig():
    print("Oink!")

if __name__ == "__main__":
    if sys.argv[1] == 'dog':
        dog()
    elif sys.argv[1] == 'cat':
        cat()
    elif sys.argv[1] == 'cow':
        cow()
    elif sys.argv[1] == 'pig':
        pig()  
    else:
        default()
