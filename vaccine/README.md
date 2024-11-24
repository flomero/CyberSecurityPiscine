# Vaccine
A little program to find possible sql injection in a given Website
It is optimized to work with **mysql** and **sqlite** databases, but also scans for some generic exploits in others. At the moment it only can do boolean, union and error based injections, but this can be changed in *testpayloads.py*.

## Usage:
```bash
vaccine [-h] [-X {GET,POST}] [-o FILE] [-v] [-l N] [-a AGENT] url
```

### Positional arguments:
```
  url                   The url to test
```

### Options:
```
  -h, --help            show this help message and exit
  -X {GET,POST}, --request {GET,POST}
                        The request to send
  -o FILE, --output FILE
                        The output file to save the result
  -v, --verbose         Enable verbose mode
  -l N, --limit-diff N  Limit the number of different lines to show
  -a AGENT, --agent AGENT
                        The user agent to use
```

> [!WARNING]
> This project is for educational purposes only. You should never use this type of program for malicious purposes. Only use it to test your own websites. The author does not take any responsibility for any damage caused by this program.