'''

Reverse a string

Input: string of length > 0
Output: reversed string

'''

# Method 1 - List comprehensions
def reverse(s):
    return "".join([l for l in s[::-1]])




# Run test cases for a given method
def test(method):
    test_cases = [
        'hello',
        '',
        'something longer with spaces',
        '12512345097',
    ]

    for t in test_cases:
        result = False
        output = None
        try:
            output = method(t)
            result = True
            print()

        except Exception as e:
            output = e

        finally:
            print(f'Test Case {test_cases.index(t)} "{t}" {result} with returned value "{output}"')