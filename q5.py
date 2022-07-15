"""
Question 5
Hamming distance is the number of characters that differ between two strings.
To illustrate:
String1: "abcbba"
String2: "abcbda"
Hamming Distance: 1 - "b" vs. "d" is the only difference.
Create a function that computes the hamming distance between two strings.
Examples
hamming_distance("abcde", "bcdef") ➞ 5
hamming_distance("abcde", "abcde") ➞ 0
hamming_distance("strong", "strung") ➞ 1
"""

def hamming_distance(s1,s2):
    if len(s1) != len(s2):
        return "Length of both strings is not equal"
    h = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            h = h + 1
    return h

s1 = input("Enter string 1 ")
s2 = input("Enter string 2 ")
h = hamming_distance(s1,s2)
print("hamming_distance(",s1,",",s2,") ➞",h)