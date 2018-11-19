from pprint import pprint as pp

line = '=' * 30
monday = [2, 3, 4, 5, 6, 8, 9]
tuesday = [6, 7, 2, 1, 6, 8, 3]
sunday = [1, 9, 8, 5, 6, 2, 9]

print(line)
for item in zip(sunday, monday):
    print(item)

print(line)
for item in zip(sunday, monday, tuesday):
    print (item)

daily = [sunday, monday, tuesday]
pp(daily)

print(line)
for item in zip(daily[0], daily[1], daily[2]):
    print(item)

print(line)
for item in zip(*daily):
    print(item)

print(line)
transposed = list(zip(*daily))
pp(transposed)
