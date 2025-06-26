def inFunc():
    sen = input("Enter input text: ")
    vowel = "aeiouAEIOU"
    return sen, vowel

def outFunc(sen, vowel):
    count = 0
    for char in sen:
        if char in vowel:
            count += 1

    print("vowels:", count)

if __name__ == "__main__":
    sen, vowel = inFunc()
    outFunc(sen, vowel)