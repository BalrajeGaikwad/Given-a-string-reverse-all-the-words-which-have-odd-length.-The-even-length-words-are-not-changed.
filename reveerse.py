"""
7. Given a string, reverse all the words which have odd length. The even length words are not changed.

Examples
reverse_odd("Bananas") ➞ "sananaB";

reverse_odd("One two three four") ➞ "enO owt eerht four";
"""
 

def revrse_word(senternce):
    words=senternce.split()
    result=[]

    for word in words:
        if len(word) % 2 !=0:
            result.append(word[::-1])
        else:
            result.append(word)

    return " ".join(result)

print(revrse_word("Bananas"))