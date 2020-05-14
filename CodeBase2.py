def is_palindrome(text):
    # Set left index to 0, set right index to the last index of the given text
    left = 0
    right = len(text) - 1

    while left < right:
        # Set left_char the character at the left index in text, Set right_char the character at the right index in text
        left_char = text[left]
        right_char = text[right]

        # Check if left_char is an alphabet character
        if not left_char.isalpha():
            # If it's not, we don't care for it so we increase left index by 1
            left += 1
            # continue on to the next iteration of the loop
            continue

        # Check if right_char is an alphabet character
        if not right_char.isalpha():
            # If it's not, we don't care for it so we increase right index by 1
            right -= 1
            # continue on to the next iteration of the loop
            continue

        # Compare the two letters to see if they are the same
        if left_char.lower() == right_char.lower():
            # If they are the same, increase/decrease the indexes
            left += 1
            right -= 1
            continue
        else:
            # If they're not, return false since this text is not a palindrome
            return False

    return True
