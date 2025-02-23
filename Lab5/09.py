#Task 9

import re

text_to_match = "Hello, world. ThisIs_A_SampleString"

pattern = r'([a-z])([A-Z])'  
replacement = r'\1 \2' 

result = re.sub(pattern, replacement, text_to_match)

print(result)