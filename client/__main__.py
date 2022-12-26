from project.core.my_func import add_one
from util import foo


def main():
    print(f"3 + 1 = " + str(add_one(3)))
    foo()


if __name__ == '__main__':
    main()
