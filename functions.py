# def is_palindrome(string):
#     backwards = string[::-1]
#     return backwards == string
# word = input("Please enter a word to chec")
# if is_palindrome(word.lower()):
#     print("{} This is in fact a palindrome".format(word))
def is_sentence_palindrome(string):
    thing = ''
    for char in string:
        if char.isalnum():
            thing+=char
    backwards = thing[::-1]
    return backwards == string
print(is_sentence_palindrome("My name is khan"))