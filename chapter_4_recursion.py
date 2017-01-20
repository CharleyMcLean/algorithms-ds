from chapter_3_stacks import Stack

def to_string(num, base):
    """Convert number to its string representation for any base
    between 2 and 16"""
    # string used to convert the integer to its corresponding string rep.
    conversion_string = "0123456789ABCDEF"

    # define our base case, which is if n is less than the base.
    # e.g. if base 10, if our num was a single int.
    if num < base:
        return conversion_string[num]
    else:
        # This will call the function on all digits but the last, added
        # to the last digit (last digit obtained using modulo)
        return to_string(num // base, base) + conversion_string[num % base]
