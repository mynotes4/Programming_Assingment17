"""
Question3. Create a function that replaces all the vowels in a string with a specified
character.
Examples
replace_vowels("the aardvark", "#") ➞ "th# ##rdv#rk"
replace_vowels("minnie mouse", "?") ➞ "m?nn?? m??s?"
replace_vowels("shakespeare", "*") ➞ "sh*k*sp**r*"
"""

def replace_vowels(s,v):
    s1 = '\"'
    for i in range(len(s)):
        if s[i] not in 'aeiou':
            s1 = s1 + s[i]
        else:
            s1 = s1 + v
    s1 = s1 + '\"'
    return s1

s = input("Enter string ")
v = input("Enter character to be replaced ")
s1 = replace_vowels(s,v)
print("replace_vowels(",s,",",v,") ➞",s1)