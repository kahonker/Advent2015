import re
import hashlib

with open("input4", "r") as f:
    data = f.read()

    
i = 0
while True:
    text = f"{data}{i}"
    md5_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
    if re.match(r"^000000", md5_hash):
        print(i)
        break
    i += 1