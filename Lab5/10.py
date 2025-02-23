#Task 10

import re

text_to_match = "Hello, world. ThisIs_A_SampleString"

pattern = r'(?<!^)(?=[A-Z])'  
replacement = '_'

result = re.sub(pattern, replacement, text_to_match).lower()  

print(result)