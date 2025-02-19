#Task2
import re

text_to_match = "A babbling baby boy bounced around."
pattern = 'ab{2,3}'

result = re.search(pattern, text_to_match)

print(result)