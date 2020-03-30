def main():
    """
    Усі ключі у словнику повинні бути унікальними.
    Якщо звернутися до ключа, якого в словнику немає,
    то з'явиться винятон KeyError
    """
    d1 = {"1": 1, "1": 2}
    print(d1)

    try:
        print(d1["3"])
    except KeyError as e:
        print(f"Couldn't find value with key: {e}")


if __name__ == "__main__":
    main()
