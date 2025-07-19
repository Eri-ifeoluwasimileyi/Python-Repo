def middle_word(word):
    length = len(word)
    half = length // 2
    if word[half:] == word[-half:]:
        return word[:half] + 'ce' + word[half:]
    else:
         return word + 'ce'
print(middle_word("helloo"))


def middle_word2(word):
    word = "helloo"
    new_word = list(word)
    new_word.insert(len(new_word)//2, "ce")
    return "".join(new_word)

print(middle_word2('helloo'))

def middle_word3(word):
    word = "helloo"
    if len(word) % 2 == 0:
        return word[:len(word)//2] + "ce" + word[len(word)//2:]
    else:
        return word + "ce"

print(middle_word3('helloo'))























