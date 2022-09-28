# freezer

check how cool are your domain lists 😎 

This is a work in progress - the whois query has lots of limitations. It still
can be useful to identify *some* expired domains.

## run

```
git clone https://github.com/citizenlab/test-lists ../test-lists
pip3 install -r requirements.txt
./freezer.py ../test-lists/lists/mx.csv
[...]
Failed domains (may include false positives, need manual check)
---------------------------------------------------------------
users.telenet.be
themexicomonitor.com
www.saludymedicinas.com.mx

failed: 1.26%

Expired domains
--------------
www.ntv.com.mx
nacionalistas.mx
www.rotativodigital.com.mx

expired: 1.26%
```

As you can see, the info we get from the whois service is not always accurate.

## related tools

- https://github.com/bassosimone/gardener
- https://github.com/gr3atest/excludeparked

# research

- https://github.com/ooni/probe/issues/1826
- https://www.securitee.org/files/parking-sensors_ndss2015.pdf


