def Fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
    
def eccentricity(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Semi-major axis (a) and semi-minor axis (b) must be positive.")
    return (1 - (b**2 / a**2)) ** 0.5