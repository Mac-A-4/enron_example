import emails

print("Width: {}".format(emails.matrix.width))
print("Height: {}".format(emails.matrix.height))

"""
We want to know if there exists a person who sent emails to 20 other people.
"""
N = 40 #other people

for i in range(emails.matrix.width): #for each person
	connections = 0
	for j in range(emails.matrix.height): #for each connection
		if emails.matrix[j,i] == 1: #there is a connection
			connections += 1
	if connections >= N:
		print("The statement is True, Person #{}".format(i))
		break
else: #python thing, happens if the for loop exits without "break"
	print("The statement is False")
