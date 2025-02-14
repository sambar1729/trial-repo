from main import Solution
# Define test cases
def test_isOneBitCharacter():
    solution = Solution()
    
    test_cases = [
        ([1, 0, 0], True),  # Last character is 1-bit
        ([1, 1, 1, 0], False),  # Last character is part of a 2-bit character
        ([0], True),  # Single one-bit character
        ([1, 1, 0], True),  # Last character is one-bit
        ([1, 0], False),  # Last character is part of a 2-bit character
        ([1, 1, 1, 1, 0, 0], True),  # Last character is 1-bit
        ([1, 1, 1, 1, 0], False),  # Last character is part of a 2-bit character
    ]

    for i, (bits, expected) in enumerate(test_cases):
        result = solution.isOneBitCharacter(bits)
        print(f"Test case {i+1}: bits={bits} | Expected={expected} | Got={result} | {'PASS' if result == expected else 'FAIL'}")


if __name__ == '__main__':
    test_isOneBitCharacter()
