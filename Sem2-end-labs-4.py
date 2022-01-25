# Yongdong Xi
# given a number and you will need to return it as a string in Expanded Form.
def expanded_form(num):
    result = []
    # A blank list is used to add elements to the result, which is represented by a list
    for index, digit in enumerate(str(num)[::-1]):
        # Using index to sort different digits
        if int(digit) != 0:
            result.append(digit + ('0' * index))
            # Add to the list in order。0 times index to show integer digits

    return ' + '.join(result[::-1])
    # When you arrive, you can sort from large to small, and each element is connected with a plus sign
 