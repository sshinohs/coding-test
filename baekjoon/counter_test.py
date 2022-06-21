# def countLetters(word):
#     counter = {}
#     for letter in word:
#         if letter not in counter:
#             counter[letter] = 0
#         counter[letter] += 1
#     return counter


# print(countLetters('hello world'))

#######################################

# from collections import Counter

# print(Counter('hello world'))

#######################################

# from collections import Counter

# def find_max(word):
#     counter = Counter(word)
#     max_count = -1
#     for letter in counter:
#         if counter[letter] > max_count:
#             max_count = counter[letter]
#             max_letter = letter
#     return max_letter, max_count

# find_max('hello world')

####################################

from collections import Counter

print(Counter('hello world').most_common())