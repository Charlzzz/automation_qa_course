import pytest


@pytest.mark.run(order=2)
def test_method1():
    print("Method 1")

def test_method2():
    print("Method 2")

@pytest.mark.run(order=1)
def test_method3():
    print("Method 3")

def test_method4():
    print("Method 4")

def test_method5():
    print("Method 5")

def test_method6():
    print("Method 6")



