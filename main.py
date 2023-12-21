import sys


def file():
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')


def main():
    pass


if __name__ == '__main__':
    file()
    main()