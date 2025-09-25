"""
caesar.py
A module for Caesar cipher encryption and decryption.
"""
import argparse
import string
from typing import Union

ALPHABET_SIZE = 26
ALPHA_LOWER = string.ascii_lowercase
ALPHA_UPPER = string.ascii_uppercase

def shift_char(ch: str, shift: int) -> str:
    """Shift a single character by `shift` positions, preserving case."""
    if ch in ALPHA_LOWER:
        idx = (ALPHA_LOWER.index(ch) + shift) % ALPHABET_SIZE
        return ALPHA_LOWER[idx]
    if ch in ALPHA_UPPER:
        idx = (ALPHA_UPPER.index(ch) + shift) % ALPHABET_SIZE
        return ALPHA_UPPER[idx]
    return ch

def caesar_cipher(text: str, shift: int) -> str:
    """Encrypt or decrypt a string using the Caesar cipher."""
    return "".join(shift_char(c, shift) for c in text)

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Encrypt or decrypt text using the Caesar cipher."
    )
    parser.add_argument(
        "mode", choices=["enc", "dec"], help="enc to encrypt, dec to decrypt"
    )
    parser.add_argument(
        "shift", type=int, help="Shift amount (e.g., 3 for classic Caesar)"
    )
    parser.add_argument(
        "text", help="Text to encrypt or decrypt (use quotes for spaces)"
    )
    return parser.parse_args()

def main():
    args = parse_args()
    shift = args.shift if args.mode == "enc" else -args.shift
    result = caesar_cipher(args.text, shift)
    print(result)

if __name__ == "__main__":
    main()
