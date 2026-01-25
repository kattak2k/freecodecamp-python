
def number_pattern(n):
    number_list = []
    if not isinstance(n,int):
       return("Argument must be an integer value.")
    elif n < 1:
       return("Argument must be an integer greater than 0.")

    for x in range(n):
        number_list.append(str(x + 1))
    
    return " ".join(number_list)

#print(number_pattern(12))
