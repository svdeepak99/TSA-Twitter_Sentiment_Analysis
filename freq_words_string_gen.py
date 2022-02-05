import string

STRING_LIMIT = 256

with open("word_list.txt", "r") as f:
    data = f.read().splitlines()

# data = data[:120]

limit_count = len(data[0])
limit_i = 1
for line in data:
    limit_count += len(line) + 4
    if limit_count > STRING_LIMIT:
        break
    limit_i += 1

data = data[:limit_i]

count = len(data[0])
final_string = data[0]

for line in data[1:]:
    count += len(line) + 4
    print(line)
    final_string += " OR " + line

print("Final Count:", count)
print("Final Length:", len(final_string))

with open("final_string.txt", "w") as f:
    f.write(final_string)

