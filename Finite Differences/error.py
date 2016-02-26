import numpy as np

# Functions of x.
def f(x):
    return 4 * pow(x, 4) - 3 * pow(x, 3)
def f2(x):
    return np.cos(x)

# Second order derivatives wrt. x.
def d2f(x):
    return 48 * pow(x, 2) - 18 * x
def d2f2(x):
    return -1 * np.cos(x)

# Finite difference func.
def approx(x, a, fn):
    return (1 / pow(a, 2)) * (fn(x - a) - 2 * fn(x) + fn(x + a))

# x to solve for.
x = 8

# Exact solution for first function.
exactSol = d2f(x)
print("Exact solution for x:", exactSol)

print("\n")

print("Approximations for x:")
for a in range(1000, 100, -100):
    print("a        = ", a/10000)
    print("solution = ", approx(x, a/10000, f))

print("\n")

# Expect this for loop to print the same value (roughly) each time, as calculating error of approximation divided by expected proportionality of that error to a.
for i in range(1000, 100, -100):
    a = i / 1000
    approxCurr = approx(x, a, f)
    print(abs(approxCurr - exactSol) / pow(a, 2))

print("\n")

# Exact solution for second function.
exactSol2 = d2f2(x)
print("Exact solution for x:", exactSol2)

print("\n")

print("Approximations for x:")
for a in range(1000, 100, -100):
    print("a        = ", a/10000)
    print("solution = ", approx(x, a/10000, f2))

print("\n")

# Expect this for loop to print the same value (roughly) each time, as calculating error of approximation divided by expected proportionality of that error to a.
for i in range(1000, 100, -100):
    a = i / 1000
    approxCurr = approx(x, a, f2)
    print(abs(approxCurr - exactSol2) / pow(a, 2))
