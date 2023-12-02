def ncr(n, r):
    if r == 0:
        return 1
    else:
        return n * 1.0 / r * ncr(n - 1, r - 1)

def main():
    n = int(input("Enter the value of N: "))
    r = int(input("Enter the value of R: "))
    
    result = ncr(n, r)
    
    print(f"The NCR value is {result:.2f}")

if __name__ == "__main__":
    main()
