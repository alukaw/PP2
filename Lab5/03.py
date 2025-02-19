#Task3

import re

text_to_match = "A_bubbly_baby_blabbled"

pattern = r'[a-z]\_'

result = re.search(pattern, text_to_match)

print(result)