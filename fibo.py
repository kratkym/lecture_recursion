def recursive_nth_fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return recursive_nth_fibo(n-1) + recursive_nth_fibo(n-2)

def main():
    n = int(input("zadejte číslo: "))
    vysledek = recursive_nth_fibo(n)
    print(f"{n}. Fibonacciho číslo je: {vysledek}")

if __name__ == "__main__":
    main()
