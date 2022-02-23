#!/usr/bin/python3

import random
import sys
import string
import requests
import json

def main(argv):
	if len(argv) < 3:
		print("Incorrect usage. Try the following: \"python strails.py <target.com> <apikey> <output_file.txt>")
		sys.exit(0)

	else:
		domain = argv[0]
		apikey = argv[1]
		out_file = argv[2]

		strails_headers = {
			"apikey" : apikey
		}

		strails_api_url = "https://api.securitytrails.com/v1/domain/" + domain + "/subdomains"
		strails_query = requests.get(strails_api_url, headers=strails_headers)
		strails_content = strails_query.content
		strails_json = json.loads(strails_content)

		subdomains = strails_json["subdomains"]

		f = open(out_file, "w")
		for subdomain in subdomains:
			subdomain_full = subdomain + "." + domain
			print(subdomain_full)
			f.write(subdomain_full + "\n")

		f.close()
		print("\n")
		print("Subdomains enumerated and written to \"" + out_file + "\".")
		print("Happy hunting!")


if __name__ == "__main__":
   main(sys.argv[1:])
