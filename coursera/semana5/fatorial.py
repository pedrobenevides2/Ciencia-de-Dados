def fatorial (x):
    b=1
    c=1

    while x>=b:
        c = c*b
        b=b+1

    
    return c


def test_fatorial ():
    assert fatorial(0)==1
    assert fatorial (1) == 1
    assert fatorial(2)==2

def test_fatorial ():
    assert fatorial (1) == 1

def test_fatorial ():
    assert fatorial(2)==2