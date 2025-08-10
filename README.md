# hash-bruteforce-tool
# Hash Cracker

A simple Python program to crack hashed passwords using either a numeric brute-force attack or a wordlist attack.

## Features

- Supports MD5, SHA1, and SHA256 hash types.
- Two modes of attack:
  - Numeric brute force (specify a start and end range).
  - Wordlist attack (using a custom wordlist file).
- Handles common errors such as missing wordlist files.

## Usage

1. Run the script.
2. Enter the target hash.
3. Enter the hash type (`md5`, `sha1`, or `sha256`).
4. Choose the attack mode:
   - Enter `1` for numeric brute force.
   - Enter `2` for wordlist attack.
5. Follow prompts based on the chosen mode.

## Example

```bash
enter the hash here: 5d41402abc4b2a76b9719d911017c592
enter the hash Type: md5
If you want to Normal attack enter 1 and if you want wordlist attack enter 2:1
enter start number: 0
enter end number: 9999
[✔] The password is: 0000
```

## Requirements

- Python 3.x

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Created by Melek Kateb

