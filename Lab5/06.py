#Task6

import re

text_to_match = "Hello, world. ThisIs_A_SampleString"

pattern = r'[ ,.]'

result = re.sub(pattern, ':', text_to_match)

print(result)