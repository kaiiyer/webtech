#!/usr/bin/env python3
import webtech

# you can use options, same as from the command line
wt = webtech.WebTech(args=None)

# scan a single website
report = wt.start_from_url('https://google.com', timeout=1)
print(report)

# scan multiple websites from a list 
for site in ['https://example.com', 'http://connectionerror']:
    try:
        report = wt.start_from_url(site, timeout=10)
        print("Site: {}".format(site))
        print(report)
    except webtech.utils.ConnectionException:
        print("Site unavailable: {}".format(site))

print("Done")
