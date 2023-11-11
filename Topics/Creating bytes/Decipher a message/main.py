def decipher(message, key):
    deciphered_ints = (code_point + key for code_point in message)
    return bytes(deciphered_ints).decode()


def main():
    message = input().encode()
    key = sum(
        int(input()).to_bytes(2, 'big')
    )
    print(decipher(message, key))


if __name__ == "__main__":
    main()
