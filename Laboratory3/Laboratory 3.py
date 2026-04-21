def heron_sqrt(S, precision=1e-10):
    if S < 0:
        return None
    if S == 0:
        return 0

    # x0
    if S > 1:
        x = S / 2 
    else:
        x = 1.0
    
    while True:
        xnext = 0.5 * (x + S / x)
        if abs(x - xnext) < precision:
            break
        x = xnext
    return x

def check(approx, real):
    if approx > real:
        print("Overestimate")
    elif approx < real:
        print("Underestimate")
    else:
        print("Exact")


# Main Programm
S = int(input("S = "))
result = heron_sqrt(S)
real_result = S**0.5

print(f"Approximation of sqrt({S}) : {result}")
print(f"Real Value : {real_result}")
check(result, real_result)