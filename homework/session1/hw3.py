str1 = "<<>>"
str2 = "hello"
result = str1 [2:] + str2 + str1 [:2]
print (result)

str3 = "aabb"
str4 = "hello"
result = str3 [:2] + str4 + str3 [2:]
print (result)