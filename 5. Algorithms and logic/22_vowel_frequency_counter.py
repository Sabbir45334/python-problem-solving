# find vowels in a string and write which vowels are present in the string and how many times each vowel appears.

def find_vowels(s):
    vowels = 'aeiouAEIOU'
    vowel_count = {}

    for char in s:
        if char in vowels:
            if char in vowel_count:
                vowel_count[char] += 1
            else:
                vowel_count[char] = 1

    return vowel_count
print("Enter a string to find the vowels and their counts:")

user_input = input()
vowel_counts = find_vowels(user_input)

for vowel, count in vowel_counts.items():
    print(f"The vowel '{vowel}' appears {count} times.")
    # print("the vowel", vowel, "appears", count, "times.")
   