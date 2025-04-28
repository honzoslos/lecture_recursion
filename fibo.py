def recursive_nth_fibo(position):
    if position == 0:
        return 0
    elif position == 1:
        return 1
    else:
        return recursive_nth_fibo(position -1) + recursive_nth_fibo(position -2)


def main():
    print(recursive_nth_fibo(12))


if __name__ == "__main__":
    main()
