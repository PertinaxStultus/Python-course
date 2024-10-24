
str_list = input("Enter the strings: ").split(',')
chr_list = input("Enter the characters to search (separated by spaces): ").split()

frequency_dict = {char: 0 for char in chr_list}

for string in str_list:
    for char in string:
        if char in frequency_dict:
            frequency_dict[char] += 1

print(frequency_dict)
