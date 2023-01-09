import pytest


@pytest.fixture()
def set_up():
    print("enter system")
    yield
    print("Exit system")

@pytest.fixture(scope="function")
def some():
    print("Start")
    yield
    print("End")






