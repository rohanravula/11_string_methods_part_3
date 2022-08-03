# a="hello","python","programming"
# print(type(a)) #tuple
# b=" world ".join(a) #if we give space to world
# print(b) #hello world python world programming. this join method joins the two strings.
# c="hello","python","programming"
# d="world".join(c)
# print(d) #helloworldpythonworldprogramming. when we will not give any space so the output will be like this

# e="hey"
# f="*".join(e)
# print(f) #h*e*y
# g="bye"
# h="6".join(g)
# print(h) #b6y6e

# i="hey",
# j="$".join(i)
# print(j) #hey. coz  after comma(,) some thing string should be their oresle the output hits same back.
# i="hey"," "
# j="$".join(i)
# print(j) #hey$. after comma their is an empty str so it give correct output. not only empty str it can any string.


# a="python programming"
# print(a.removeprefix("p")) #ython programming
# b="programming language"
# print(b.removeprefix("pro")) #gramming language. this removeprefix method is used to remove the first letter.

# c="rohan"
# print(c.removesuffix("n")) # roha.  this method is used to remove the last word.
# d="vijay kumar"
# print(d.removesuffix("mar")) #vijay ku.

# print("rohankumar007".isalnum()) #True. alnum should contain only the alaphebets and numbers.And their should not be a space betewwn them.
# print("rohan 007".isalnum()) #False. it shows false coz it is having space.
# print("rohan".isalnum()) #True. coz the alnum should contain the alpabets.
# print("858".isalnum()) #True. coz the alnum should contain the numbers.
# print("hii_rohan".isalnum()) #False. coz in the alnum no special charater is used.

# print("rohankumar".isalpha()) #True. in isalpha it should contain only the alpabets only and no any numbers and no any spl charaters.
# print("Rohan".isalpha()) #True.
# print("rohan007".isalpha()) #False. coz it contains the number so it is flase.
# print("rohan_kumar".isalpha()) #False. coz it contains the spl charaters.
# print("rohan kumar".isalpha()) #False. coz it contains the space.

# print("hii hello_007".isascii()) #isascii represents always true.

# b=chr(0)
# c=chr(32)
# print(b.isspace()) #False
# print(c.isspace()) #True

# #this just to show that how many ways we can write this.
# print("hello"+chr(32)+"python") #hello python
# print("hello"+' '+"python") #hello python
# print("hello","python") #hello python
# print("hello","python",sep=" ") #hello python
# print(chr(0)+"hey") #hey. without space hey
# print(chr(32)+"hey") # hey . with space hey


# print(ord("A")) #65
# print(ord("a")) #97
# print(ord("z")) #122
# print(ord("Z")) #90
# print(ord("0")) #48
# print(ord("9")) #57
# print(ord(" ")) #32
# print(ord("!")) #33
print(chr(97)) #a
print(chr(99)) #c
print(chr(65)) #A
print(chr(69)) #E