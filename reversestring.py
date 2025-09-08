def rev_using_stack(s):
    stack = []
    for char in s:
        stack.append(char)
    reverse_str = ""
    while stack:
        reverse_str += stack.pop()
    return reverse_str

def reverse_str(s):
    reverse_string = ""
    for i in range(len(s)-1,-1,-1):
        reverse_string += s[i]
    return reverse_string

if __name__ == "__main__":
    input_str = input("Enter String: ")

    print(f"Output using stack: {rev_using_stack(input_str)}")
    print(f"Output: {reverse_str(input_str)}")
