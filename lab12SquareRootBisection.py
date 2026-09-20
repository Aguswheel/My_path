def square_root_bisection(number, tolerance=1, max_iter=5):
    if number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    if number == 0 or number == 1:
        print(f"The square root of {number} is {number}")
        return number
    low = 0.0
    high = max(1.0, number)
    root = None
    for _ in range(max_iter):
        mid = (low + high) / 2
        square_mid = mid ** 2 
        if (high - low) <= tolerance:
            root = mid
            break
        elif square_mid < number:
            low = mid
        else:
            high = mid
    if root is None:
        print(f"Failed to converge within {max_iter} iterations")
        return None
    else: 
        print(f"The square root of {number} is approximately {root}")
        return root
