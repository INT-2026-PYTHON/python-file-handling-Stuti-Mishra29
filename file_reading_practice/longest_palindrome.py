"""
## 5. Longest Palindrome in the File  *(Hard)*

=================================================
LONGEST PALINDROME
=================================================

Problem Statement:
Read the text file `sowpods.txt` and find the
LONGEST PALINDROME word in the file.

If multiple palindromes share the maximum
length, print ALL of them.

-------------------------------------------------
Input Example (sowpods.txt sample):
level
radar
noon
civic
deified
racecar
rotator
malayalam

Output Example:
Longest palindrome length: 9
malayalam

-------------------------------------------------
Explanation:
Lengths of the palindromes in the sample:
   level    -> 5
   radar    -> 5
   noon     -> 4
   civic    -> 5
   deified  -> 7
   racecar  -> 7
   rotator  -> 7
   malayalam -> 9
The longest is "malayalam" with 9 characters.
=================================================

"""
# Function to check if a word is a palindrome
def is_palindrome(word):
    return word == word[::-1]


def find_longest_palindromes(filename):
    longest_words = []
    max_length = 0

    with open(filename, "r") as file:
        for line in file:
            word = line.strip().lower()  

            if is_palindrome(word):
                word_length = len(word)

                if word_length > max_length:
                    max_length = word_length
                    longest_words = [word]

                elif word_length == max_length:
                    longest_words.append(word)

    return max_length, longest_words


filename = "sowpods.txt"
max_len, palindromes = find_longest_palindromes(filename)

print("Longest palindrome length:", max_len)
for word in palindromes:
    print(word)