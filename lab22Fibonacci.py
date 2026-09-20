def fibonacci(n):
    sequence = [0, 1]
    if n < 2:
        return sequence[n]
    for f in range(2, n + 1):
        next_value = sequence[f - 1] + sequence [f - 2]
        sequence.append(next_value)
    return sequence[n]

