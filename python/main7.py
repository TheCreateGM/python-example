def palind(s):
    return s == s[::-1]

def longpalind(text):
    longest = ""
    n = len(text)

    for i in range(n):
        for j in range(i + 1, n + 1):
            part = text[i:j]
            if palind(part) and len(part) > len(longest):
                longest = part

    return longest

if __name__ == "__main__":
    word = input("Enter word: ")
    print("long palindrome:", longpalind(word))