#Task 8

import re

text_to_match = "Hello, world. ThisIs_A_SampleString"

pattern = r'[A-Z][^A-Z]*'

result = re.findall(pattern, text_to_match)

print(result)