#Task4

import re

text_to_match = "Apple blossoms bloom beautifully beside a bright blue barn"

pattern = r'[A-Z]\w+'

result = re.search(pattern, text_to_match)

print(result)