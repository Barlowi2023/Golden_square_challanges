from lib.Counter import *

def test_counter1():
    counter = Counter()
    counter.add(5)
    result = counter.report()
    assert result == "Counted to 5 so far."

def test_counter2():
    counter = Counter()
    counter.add(12)
    result = counter.report()
    assert result == "Counted to 12 so far."


def test_counter3():
    counter = Counter()
    counter.add(5)
    counter.add(5)
    result = counter.report()
    assert result == "Counted to 10 so far."


def test_counter4():
    counter = Counter()
    result = counter.report()
    assert result == "Counted to 0 so far."  

def test_counter5():
    counter = Counter()
    counter.add(-4+1)
    # counter.add(5)
    result = counter.report()
    assert result == "Counted to -3 so far."