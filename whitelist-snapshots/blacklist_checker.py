with open("input.txt", "r") as input_file:
    input_lines = input_file.readlines()

with open("blacklist.txt", "r") as blacklist_file:
    blacklist_lines = set(line.strip() for line in blacklist_file)

whitelist_lines = [line for line in input_lines if line.strip() not in blacklist_lines]

with open("whitelist.txt", "w") as whitelist_file:
    whitelist_file.writelines(whitelist_lines)