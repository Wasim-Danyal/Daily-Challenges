def challenge (thisset):
	asd = list(dict.fromkeys(thisset))
	answer = " ".join(sorted(asd))
	return answer
	
x = input("here: ")
word = x.split()
print(challenge(word))