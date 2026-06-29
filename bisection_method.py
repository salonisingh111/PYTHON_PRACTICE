def square_root_bisection(number,tolerance=1e-7,max_iterations=100):
    if number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    
    if number==0 and number==1:
        print(f"The square root of {number} is {number}")
        return float(number)
    low = 0 if number >= 1 else number
    high = number if number >= 1 else 1
    
    root = (low + high) / 2
    
    for i in range(max_iterations):
        if abs(root**2 - number) <= tolerance:
            print(f"The square root of {number} is approximately {root}")
            return root
        
        if root**2 < number:
            low = root
        else:
            high = root
        
        root = (low + high) / 2
        
    print(f"Failed to converge within {max_iterations} iterations")
    return None   