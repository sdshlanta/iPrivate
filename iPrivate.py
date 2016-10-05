#!/usr/bin/python
import shodan
import socket
from ipwhois import IPWhois
import libnmap
import argparse
import os
import json
from pprint import PrettyPrinter as pp
def performNmapScan(ip):
	p = pp(indent=4).

def performShodanLookup(ip):


def performIPWhoisLookup(ip):
	print("Attempting to find information on the owner of %s" % ip)
	try:
		lookup = IPWhois(ip)
	except ValueError as e:
		print("%s does not appear to be an IPv4 or IPv6 address" % ip)
		return
	except Exception as e:
		raise e

	return lookup.lookup_rdap()

def main():
	collectedInfo = {}

	iwhois = performIPWhoisLookup(args.ip)
	print(iwhois)



if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="A tool for finding out information on a given IP address(ownership, assocated domain names, countries).")
	parser.add_argument('ip', help='the IP you would like to lookup')
	args = parser.parse_args()
	print args.ip
	main()
