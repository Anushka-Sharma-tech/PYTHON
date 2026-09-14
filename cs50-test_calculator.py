# INTRODUCING UNIT TESTING USING PYTEST

from cs50_calculator import square 
def main():
    test_square()
def test_square():
        assert square(2)==4
        assert square(-2)==4
        assert square(3)==9
        assert square(-3)==9
        assert square(0)==0
    
if __name__=="__main__":
    main()
# Use this command to check with pytest 
# python -m pytest cs50-test_calculator.py 