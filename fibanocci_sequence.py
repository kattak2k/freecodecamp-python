#Recursive tabular
# style 1 : sequence as lise
sequence = [0,1]
def fibonacci(n):
    if n < 0:
        return "-"
    if n < len(sequence):
        return sequence[n]
    result = fibonacci(n - 1) + fibonacci(n - 2)
    sequence.append(result)
    return(result)
print(fibonacci(7))


# style 2 : sequence as dictionary
sequence = {0: 0, 1: 1}

def fibonacci(n):
    if n < 0:
        return "-"
    if n not in sequence:
        sequence[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return sequence[n]

print(fibonacci(3))  # 2
print(fibonacci(7))  # 13

# mon- recursive
def fibonacci(n):
    sequence = [0, 1]
    if n < 0:
        return "-"
    while len(sequence) <= n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[n]


print(fibonacci(3))  # 2
print(fibonacci(7))  # 13
