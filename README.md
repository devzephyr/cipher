
# Caesar Cipher

This project provides a simple, robust implementation of the Caesar cipher in Python. The Caesar cipher is a classic encryption technique that shifts each letter in the plaintext by a fixed number of positions in the alphabet.

## Features
- Encrypt and decrypt messages using a shift value
- Preserves case (uppercase/lowercase)
- Non-alphabetic characters are not changed
- Command-line interface for easy use
- Well-structured, type-annotated code

## Usage

### Command Line

```bash
python caesar.py enc 3 "Meet me at 10"
python caesar.py dec 3 "Phhw ph dw 10"
```

- `enc`: Encrypt the message
- `dec`: Decrypt the message
- `3`: The shift amount (can be any integer)
- The text must be in quotes if it contains spaces

### Example

Encrypt:
```bash
python caesar.py enc 5 "Hello, World!"
# Output: Mjqqt, Btwqi!
```

Decrypt:
```bash
python caesar.py dec 5 "Mjqqt, Btwqi!"
# Output: Hello, World!
```

## Module Usage

You can also import and use the cipher in your own Python code:

```python
from caesar import caesar_cipher

encrypted = caesar_cipher("Secret Message", 4)
decrypted = caesar_cipher(encrypted, -4)
print(encrypted)  # Output: Wigvix Qiwweki
print(decrypted)  # Output: Secret Message
```

## Requirements
* Python 3.6 or higher
* No external dependencies

## License
See [LICENSE](LICENSE) for details.
