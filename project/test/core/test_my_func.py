from project.core.my_func import add_one, add_two


def test_add_one():
    assert add_one(5) == 6
    assert add_one(0) == 1
    assert add_one(-3) == -2


def test_add_two():
    assert add_two(5) == 7
    assert add_two(0) == 2
    assert add_two(-3) == -1
