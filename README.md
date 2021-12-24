# terraform-external-pyurlparse
#

This a python fork of https://github.com/matti/terraform-external-urlparse,
which depends on python rather than ruby.

The main motivation for this fork is that I already manage a number
of python stacks, and this means I don't need to add a build dependency
on ruby 

Examples of use:
```
module "test" {
  source = "rgammans/pyurlparse/external"
  url = "http://user:pass@www.example.com:8080/path?query1=1&query2=2#frag"
}
```
which has tf outputs:
```
Outputs: (as per urllib.parse.urlparse )

fragment = frag
password = pass
path = /path
query = query1=1&query2=2
scheme = http
username = user 
password = pass, 
hostname = www.example.com
port = 8080
netloc= user:pass@www.example.com:8080

```
