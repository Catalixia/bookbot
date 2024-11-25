

#Counting words
with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    words = file_contents.split()
    count = len(words)
    

#Counting letters
letters_dict = {}
for char in file_contents:
    if char.isalpha():
        char = char.lower()
        if char in letters_dict:
            letters_dict[char] += 1
        else:
            letters_dict[char] = 1

#Sorting dictionarys
sorted_letters = {key: value for key, value in sorted(letters_dict.items(), key=lambda item: item[1], reverse=True)}

#report to print
print("--- Begin report of books/frankenstein.txt ---")
print(f"{count} words found in the document")
print("")
for key, value in sorted_letters.items():
    print(f"The {key} character was found {value} times")

print("--- End report ---")