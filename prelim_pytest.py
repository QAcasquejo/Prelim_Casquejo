import math

def test_grade():
    grade = 50

    assert grade>=50

def test_temperature():
    c = 40
    f = 20
    assert c/f == 2

def test_areaSquare():
    length=8
    width=9
    height=9

    assert length*width*height == 648