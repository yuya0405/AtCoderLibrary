from collections import defaultdict
d = defaultdict(int)

for key in val_str:
    d[key] += 1

print(d)
