from custom_calculator import add, substract, multiple, divide

def test_add():
    assert add(5,1) == 6

def test_substract():
    assert substract(5,1) == 4

def test_multiple():
    assert multiple(2025, 5) == 10125

def test_divide():
    assert divide(2025,5) == 405

