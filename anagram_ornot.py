def are_anagram(str1,str2):
    str1 = str1.replace(" ","").lower()
    str2 = str2.replace(" ","").lower()
    return sorted(str1)==sorted(str2)
string1=input("enter the first word")
string2=input("enter the second word")
if are_anagram(string1,string2):
    print(f"{string1} and {string2} are anagram")
else:
    print(f"{string1} and {string2} are not anagram")
