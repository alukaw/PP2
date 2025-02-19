#Task1

import re 

text_to_match = "Lorem Ipsum abb has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."

pattern = 'ab*'

result = re.search(pattern, text_to_match)

print(result)

