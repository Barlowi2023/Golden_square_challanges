def factorial(n):
    product = n
    print(f"at the start product is {product}")
    while n > 2:
        n -= 1
        print(f"we multiply {product} by {n}")
        product *= n
        print(f"we get {product}")
      
    return product

print(f"""
 Running: factorial(5)
Expected: 120
  Actual: {factorial(5)}
""")

print(f"""
 Running: factorial(7)
Expected: 540
  Actual: {factorial(7)}
""")

print(f"""
 Running: factorial(12)
Expected: 479001600
  Actual: {factorial(12)}
""")