# Stockholm - a small harmless malware

**Usage:** `stockholm.py [-h] [-v] [-r] [-s] [-u] key`

Positional Arguments:
```plaintext
  key            The key to use for encryption.
```

options:
```plaintext
  -h, --help     show this help message and exit
  -v, --version  show program's version number and exit
  -r, --reverse  Reverse the encryption.
  -s, --silent   Silent mode.
  -u, --dry-run  Dry run (no encryption - just printing what would be done).
```

Stockholm is a simple encryption malware that uses a key to encrypt and decrypt files.
It only encrypts the files in the `./infection` folder in the user's home directory. (The user is the one who runs the program.) Files that are encrypted will be renamed with the `.ft` extension. 

> [!WARNING]
> This project is for educational purposes only. You should never use this type of program for malicious purposes. The author does not take any responsibility for any damage caused by this program.