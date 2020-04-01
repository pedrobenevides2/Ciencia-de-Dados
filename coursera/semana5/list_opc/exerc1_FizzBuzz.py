


def fizzbuzz(x):
    if x%3==0:
        if x%5!=0:
            return("Fizz")
        elif x%5==0:
            return("FizzBuzz")
    elif x%5==0:
        if x%3!=0:
            return("Buzz")
    else:
        return(x)


a= int(input(" Digite um número: "))
w=fizzbuzz(a)
print(w)