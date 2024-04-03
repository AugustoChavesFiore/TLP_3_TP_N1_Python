
def is_palindrome(word):
    word = word.lower()

    return word==word[::-1]



letras = 'aabbc'
x=[]
for i in range(len(letras)):
