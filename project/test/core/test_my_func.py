from project.core.my_func import add_one


def test_add_one():
    assert add_one(5) == 6
    assert add_one(0) == 1
    assert add_one(-3) == -2
