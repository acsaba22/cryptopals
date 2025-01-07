import base64



def main():
    hex = b'49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    bytes = base64.b16decode(hex, casefold=True)
    b64 = base64.b64encode(bytes)
    print(f'{hex=}')
    print(f'{bytes=}')
    print(f'{b64=}')

if __name__ == "__main__":
    main()
