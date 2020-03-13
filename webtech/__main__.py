#!/usr/bin/env python
import sys
import argparse

from .__version__ import __version__ as VERSION
from .webtech import WebTech

class Driver(object):

    def __init__(self,args):
        self.args = args
    
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type:
            print(exc_type, exc_value, exc_traceback)

    def driver(self):

        args = self.args


        wt = WebTech(args)
        if args.scrape:
            wt.scraping()
        else:
            if args.urls is None and args.urls_file is None and not args.update_db:
                print("No URL(s) given!")
                #args.print_help()
                exit()

            wt.start() 

"""
def split_on_comma(option, opt_str, value, parser):
    setattr(parser.values, option.dest, value.split(','))
"""
def split_on_comma(values):
    return values.split(',')


def parse_args():
    """
    Main function when running from command line.
    """
    parser = argparse.ArgumentParser(prog="webtech")
    parser.add_argument("-s" , "--scrape" , type =  str, help = "Enter the URL to scrape")
    parser.add_argument(
        "-u", "--urls",
         type=split_on_comma)
    parser.add_argument(
        "--urls-file", "--ul",
        help="url(s) list file to scan", type=str)
    parser.add_argument(
        "--user-agent", "--ua",
        help="use this user agent")
    parser.add_argument(
        "--random-user-agent", "--rua", action="store_true",
        help="use a random user agent", default=False)
    parser.add_argument(
        "--database-file", "--db",
        help="custom database file")
    parser.add_argument(
        "--json", "--oj", action="store_true",
        help="output json-encoded report", default=False)
    parser.add_argument(
        "--grep", "--og", action="store_true",
        help="output grepable report", default=False)
    parser.add_argument(
        "--update-db", "--udb", action="store_true",
        help="force update of remote db files", default=False)
    parser.add_argument(
        "--timeout", type=float, help="maximum timeout for scrape requests", default=10)

    return parser.parse_args()



if __name__ == "__main__":
    args = parse_args()

    with Driver(args) as dri:
        dri.driver()
