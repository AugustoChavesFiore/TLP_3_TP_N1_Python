def palindrome_reorder(word):
    word_dict = {}
    for letter in word:
        if letter in word_dict:
            word_dict[letter] += 1
        else:
            word_dict[letter] = 1
    odd_letter = None
    for letter in word_dict:
        if word_dict[letter] % 2 == 1:
            if odd_letter:
                print("NO SOLUTION")
                return
            odd_letter = letter
    word = ""
    for letter in word_dict:
        word += letter * (word_dict[letter] // 2)
    palindrome= word + (odd_letter if odd_letter else "") + word[::-1]
    return palindrome    
assert palindrome_reorder("aabbc") == "abcba", "Error en el caso de prueba"
assert palindrome_reorder("aaabb") == "ababa", "Error en el caso de prueba"