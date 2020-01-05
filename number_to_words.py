import inflect
x= int(input("enter the number that you want change in words:"))
p = inflect. engine()
words = p. number_to_words(x)
print(words)
words = p. number_to_words(p. ordinal(x))
print(words)
