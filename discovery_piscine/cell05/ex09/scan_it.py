import sys
import re
if len(sys.argv) != 3:
    print("none")
else:
    keyword = sys.argv[1]
    text = sys.argv[2]
    match_list = re.findall(keyword, text)
    count = len(match_list)
    if count > 0:
        print(count)
    else:
        print("none")