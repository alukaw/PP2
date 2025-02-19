#Task5

import re

text_to_match = "arat bought a big blue bag before breakfast ahdksb. He briskly walked beside a bustling bazaar, balancing the bag boldlb"

pattern = '^a.+b$'

result = re.search(pattern, text_to_match)

print(result)