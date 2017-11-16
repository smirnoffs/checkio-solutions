def checkio(expression):
    correct_pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for symbol in expression:
        if symbol in ('(', '[', '{'):
            stack.append(symbol)
        if symbol in (')', ']', '}'):
            try:
                if stack.pop() != correct_pairs[symbol]:
                    return False
            except IndexError:
                # closing brackets that were not opened
                return False
    if stack:
        return False
    return True


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
