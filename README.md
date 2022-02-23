# strails_enumeration
This is a tool designed to enumerate subdomains using the securitytrails.com API.

SecurityTrails has an extremely robust API that can be used to enumerate subdomains. It's great because they've already done all of the enumeration for us. No need for SubLister, gobuster dns, sbrute, amass or anything like that. This little script is designed to query their API and parse the results into a file that is ready to be sent to tools like GoWitness and aquatone. 

Usage is pretty simple. First you need to register at securitytrails.com and get an API key. Next, all you have to do is run the command as follows:
```
  python3 strails_enumeration.py [target.com] [apikey] [outfile]
```

![alt text](https://i.ibb.co/r0hxjpw/strails.png)

This will write all of the enumerated subdomains to the specified output file and will be ready to be passed to other tools.

Happy hunting!
