#Lenh break : dung trong for va while
for letter in 'Python':  # First Example
    if letter == 'h':
        break
    print('Current Letter :', letter)

var = 10  # Second Example
while var > 0:
    print('Current variable value :', var)
    var = var - 1
    if var == 5:
        break

print("Good bye!")

#Lenh pass :
for letter in 'Python':
    if letter == 'h':
        pass
        print('This is pass block')
    print('Current Letter :', letter)

print("Good bye! Pass")

#While ...else
count = 0
while count < 5:
    print (count, " is  less than 5")
    count = count + 1
else:
    print (count, " is not less than 5")

#For...else
