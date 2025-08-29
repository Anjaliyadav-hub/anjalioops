def swap_first_n_chars(str1, str2, n):
    # Check if both strings are long enough
    if n > len(str1) or n > len(str2):
        print("Error: 'n' is larger than one of the string lengths.")
        return None, None

    # Swap first n characters
    new_str1 = str2[:n] + str1[n:]
    new_str2 = str1[:n] + str2[n:]

    return new_str1, new_str2


# Example usage
s1 = "hello"
s2 = "world"
n = 2

new_s1, new_s2 = swap_first_n_chars(s1, s2, n)

if new_s1 is not None:
    print("After swapping:")
    print("String 1:", new_s1)
    print("String 2:", new_s2)
