#!/usr/bin/env python3
import json
import urllib.parse
import os
import argparse

def get_parser():
    parser = argparse.ArgumentParser("url2json")
    parser.add_argument("url",type=str, help="The url to split into parts")
    return parser

def main():
    parsed = urllib.parse.urlparse(opts.url)
    result = parsed._asdict()
    result.update({
        k:str(getattr(parsed,k))
        for k in ['hostname','port','username','password']
    })
    print(json.dumps(result))


opts = None
if __name__ == "__main__":
    parser = get_parser()
    opts = parser.parse_args()
    main()
