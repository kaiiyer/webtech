# webtech
Identify the technologies used on websites. (Dig-deep into web tech from your terminal)

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/e1f930ad4e9049109d73459f1edb7392)](https://app.codacy.com/manual/kaiiyer47/webtech?utm_source=github.com&utm_medium=referral&utm_content=kaiiyer/webtech&utm_campaign=Badge_Grade_Dashboard)
[![CircleCI](https://circleci.com/gh/kaiiyer/webtech.svg?style=svg)](https://circleci.com/gh/kaiiyer/webtech)

## Installation
WebTech is available on pip:
```
pip install webtech
```
It can be also installed via setup.py:

```
pip install -r requirements.txt
python setup.py install --user
```

## Usage
[![Webtech Interface](https://user-images.githubusercontent.com/24914913/74858499-6fc4dc80-536b-11ea-996a-6c6b9bb20a1f.png)]

Scan a website:

```
$ webtech -u https://example.com/

Target URL: https://example.com
```
## Resources for database matching

HTTP Headers information - http://netinfo.link/http/headers.html  
Cookie names - https://webcookies.org/top-cookie-names  

## Burp Integration

Download Jython 2.7.0 standalone and install it into Burp.

In "Extender" > "Options" > "Python Environment":

    Select the Jython jar location

Finally, in "Extender" > "Extension":

    Click "Add"
    Select "py" or "Python" as extension format
    Select the Burp-WebTech.py file in this folder

PRs are always welcome !!!

Inspired by [webtech](https://github.com/ShielderSec/webtech)
