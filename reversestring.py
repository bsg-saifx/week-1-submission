def reverse_str(s):
    reverse_string = ""
    for i in range(len(s)-1,-1,-1):
        reverse_string += s[i]
    return reverse_string
if __name__ == "__main__":
    input_str = input("Enter String: ")
    print(f"Output: {reverse_str(input_str)}")
