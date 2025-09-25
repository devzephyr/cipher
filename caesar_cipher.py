import argparse
import string

ALPHA_LOWER = string.ascii_lowercase
ALPHA_UPPER = string.ascii_uppercase

def shift_char(ch, k):
    if ch in ALPHA_LOWER:
        i = (ALPHA_LOWER.index(ch) + k) % 26
        return ALPHA_LOWER[i]
    if ch in ALPHA_UPPER:
        i = (ALPHA_UPPER.index(ch) + k) % 26
        return ALPHA_UPPER[i]
    return ch  

def caesar(text, k):
    return "".join(shift_char(c, k) for c in text)

def main():
    p = argparse.ArgumentParser(description="Caesar cipher")
    p.add_argument("mode", choices=["enc", "dec"], help="enc to encrypt, dec to decrypt")
    p.add_argument("shift", type=int, help="shift amount, e.g., 3")
    p.add_argument("text", help="message")
    args = p.parse_args()

    k = args.shift if args.mode == "enc" else -args.shift
    print(caesar(args.text, k))

if __name__ == "__main__":
    main()
