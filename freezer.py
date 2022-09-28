#!/usr/bin/env python3
# Curate test lists according to whois data
# (c) Ain Ghazal 2022

import csv
import os
import sys

from datetime import datetime
from urllib.parse import urlparse

import whois


failed = []
expired = []
numDomains = 0


fieldnames = [
        'creation_date',
        'expiration_date',
]

exclude = [
        'blogspot.com',
        'blogspot.fr',
]

def secondLevel(d):
    parts = d.split(".")
    if len(parts) <= 2:
        return d
    return ".".join(parts[-2:])


def cleanupFailed():
    global failed
    failed = [d for d in failed if secondLevel(d) not in exclude]

def main(list_file):
    global numDomains
    now = datetime.now()

    with open(list_file, 'r', newline='') as csvfile:
        urlreader = csv.reader(csvfile)
        for url in urlreader:
            try:
                u = urlparse(url[0])
            except:
                print("malformed:", url)
                continue
            host = u.hostname
            if host is None:
                continue
            numDomains += 1
            try:
                print("checking ", host)
                w = whois.whois(host)
                expiry = w['expiration_date']
                if type(expiry) == list:
                    expiry = expiry[0]
                status = w.get('status')
                if status is not None:
                    if type(status) == list:
                        status = status[0]
                    status = status.lower()
                if expiry is None:
                    if status is not None:
                        print("status:", status)
                        continue
                    print("failed:", host)
                    print(w)
                    failed.append(host)
                    continue
                if expiry < now:
                    expired.append(host)
                    print("expired domain:", host, expiry)
            except Exception as e:
                print("failed:", e, host)
                failed.append(host)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: freezer.py <list_file>")
        sys.exit(1)
    list_file = sys.argv[1]
    main(list_file)
    cleanupFailed()
    if len(failed) != 0:
        print()
        print("Failed domains (may include false positives, need manual check)")
        print("---------------------------------------------------------------")
        for d in failed:
            print(d)
        print()
        print("failed: %0.2f%%" % (100.0 * len(failed)/numDomains))
        print()
    if len(expired) != 0:
        print("Expired domains")
        print("--------------")
        for d in expired:
            print(d)
        print()
        print("expired: %0.2f%%" % (100.0 * len(expired)/numDomains))
        print()
