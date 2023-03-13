def get_max_length_of_substring(s: str) -> int:
    """Returns the maximium length of the substrings of s without repeating characters."""

    # Validate contraints
    if not s or len(s) > 50000:
        raise ValueError("The length of the string should be less than 50000")

    # Create variables to store last item and max_length
    seen_characters = {}
    max_length = 0
    # starting the initial point of window to index 0
    start = 0

    for current_index in range(len(s)):

        # Checking if we have already seen the element
        current_character = s[current_index]

        if current_character in seen_characters:
            # If we have seen the number, move the start pointer
            # to position after the last occurrence
            start = max(start, seen_characters[current_character] + 1)

        # Updating the last seen value of the character
        seen_characters[current_character] = current_index
        max_length = max(max_length, current_index - start + 1)
    return max_length
