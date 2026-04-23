"""
Caesar Ciphor to encode the message. This function will both handle character shift and encoding.
"""


def char_shift(char:str, shift:int) -> str:
    """
    Shifts letters by provided shift.

    This function takes a string as an argument and an integer. Then shifts one character in the alphabet forward or backwards.  The shift is zero for non-alphabetic characters.

    Args:
        char(str): a string
        shift(int): an integer

    Returns: a string

    Example:
        >>> char_shift('a', 3)   # -> 'd' (typical shift)
        'd'
        >>> char_shift('x', 3)   # → 'a' (wrap-around)
        'a'
        >>> char_shift('A', 3)   # → 'D' (preserve case)
        'D'
        >>> char_shift('!', 3)   # → '!' (non-letter unchanged)
        '!'
        >>> char_shift('d', -3)  # → 'a' (reverse shift)
        'a'
    """
    # Validation
    if not isinstance(char, str):
        raise TypeError('char must be a string')
    if not isinstance(shift, int):
        raise TypeError('shift must be an integer')

    alphabet = "abcdefghijklmnopqrstuvwxyz"



    if char.isalpha():
        # Inside
        # that if block, your thinking should be:
            # Convert 'a' → numeric position
            # Apply shift
            # Handle wrap - around
            # Convert back to character
        new_char = char + shift
        return new_char

def main():
    pass

if __name__ == "__main__":
    main()
