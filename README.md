# Phishing Link Scanner

## Overview

Phishing Link Scanner is a Python-based tool designed to detect potential phishing URLs by analyzing their structure and identifying suspicious patterns. It checks URLs against common phishing keywords and detects anomalies such as IP addresses and excessive subdomains.

## Features

- Detects phishing-related keywords in URLs (e.g., "login", "password", "verify").
- Identifies URLs containing suspicious patterns like IP addresses.
- Scans for multiple subdomains that may indicate phishing attempts.
- Simple and efficient Python script.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/phishing-link-scanner.git
   ```
2. Navigate to the project folder:
   ```bash
   cd phishing-link-scanner
   ```
3. Run the script:
   ```bash
   python phishing_scanner.py
   ```

## Usage

Modify the `urls_to_scan` list in the script with the URLs you want to check, then run the script:

```python
urls_to_scan = [
    "http://example.com",
    "http://secure-login.example.com",
    "http://update-password.com",
    "http://go0gle.com"
]
```

### Example Output

```
████╗ ██╗  ██╗██╗███████╗██╗  ██╗██╗███╗   ██╗ ██████╗     ██╗     ██╗███╗   ██╗██╗  ██╗    ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
██╔══██╗██║  ██║██║██╔════╝██║  ██║██║████╗  ██║██╔════╝     ██║     ██║████╗  ██║██║ ██╔╝    ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
██████╔╝███████║██║███████╗███████║██║██╔██╗ ██║██║  ███╗    ██║     ██║██╔██╗ ██║█████╔╝     ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
██╔═══╝ ██╔══██║██║╚════██║██╔══██║██║██║╚██╗██║██║   ██║    ██║     ██║██║╚██╗██║██╔═██╗     ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
██║     ██║  ██║██║███████║██║  ██║██║██║ ╚████║╚██████╔╝    ███████╗██║██║ ╚████║██║  ██╗    ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚══════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
                                                                                                                                                          
██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗    ██████╗ ██╗   ██╗         ███████╗ █████╗ ███╗   ██╗ ██████╗██╗  ██╗██╗████████╗            
██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝    ██╔══██╗╚██╗ ██╔╝         ██╔════╝██╔══██╗████╗  ██║██╔════╝██║  ██║██║╚══██╔══╝            
██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║       ██████╔╝ ╚████╔╝█████╗    ███████╗███████║██╔██╗ ██║██║     ███████║██║   ██║               
██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║       ██╔══██╗  ╚██╔╝ ╚════╝    ╚════██║██╔══██║██║╚██╗██║██║     ██╔══██║██║   ██║               
██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║       ██████╔╝   ██║            ███████║██║  ██║██║ ╚████║╚██████╗██║  ██║██║   ██║               
╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝       ╚═════╝    ╚═╝            ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝╚═╝   ╚═╝               
                                                                                                                                              

Potential phishing URL detected: http://secure-login.example.com
Potential phishing URL detected: http://update-password.com
Suspicious URL detected: http://go0gle.com
URL seems safe: http://example.com
```

## Contributing

Feel free to contribute by submitting pull requests or reporting issues. Any improvements or additional detection mechanisms are welcome!

##
