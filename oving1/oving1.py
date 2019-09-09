word = "Hello world, "
name = input("Enter your name \n")
array = name.split()
initials = array[0][:1] + "." + array[1][:1]
print(initials)
print(word + name)
