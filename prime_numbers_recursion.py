

def isPrime(x : int) -> bool:

    for i in range(2, int(x**0.5)
                   + 1):
        if x % i == 0:
            return False
    return True


def main():


    x = int(input('Введите x: '))

    print(isPrime(x))    


if __name__ == "__main__":
    main()
