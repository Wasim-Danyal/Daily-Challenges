#Write a function that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
#Suppose the following input is supplied to the program: 9 Then, the output should be: 11106 (i.e. 9+99+999+9999)
#Write a test for this function.


def adder(input):
    return sum(int(input * i) for i in range(1, 5))

