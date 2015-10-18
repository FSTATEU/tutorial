"""
Module Docstring
We show how to use functions in python
"""

#
## Implement increment function inc(x)
#

def inc(x):
    return x+1

#
## Implement  function double(x) which returns 2*x
#

def double(x):
    return 2*x

def main():
    """Testing functions"""
    x = 1;
    print( inc(x)*double(x))

if __name__=='__main__':
    main()
