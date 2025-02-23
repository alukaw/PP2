#Task 7

import re

text_to_match = "Hello, world. ThisIs_A_SampleString"

words = text_to_match.split('_')
result = words[0] + ''.join(word.capitalize() for word in words[1:])

print(result)  