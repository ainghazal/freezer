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
alternativa-chiapas.blogspot.com
circulodeestudioscoapa.blogspot.com
jovenesporelsocialismooaxaca.blogspot.com
juarezenlasombra.blogspot.com
mexicoendescomposicion.blogspot.com
nuestromexicobizarro.blogspot.com
revolucionesmx.blogspot.com
users.telenet.be
themexicomonitor.com
mexicovoices.blogspot.com
www.saludymedicinas.com.mx
movimiento-sinarquista.blogspot.com

failed: 5.04%

Expired domains
--------------
www.ntv.com.mx
nacionalistas.mx
www.rotativodigital.com.mx

expired: 1.26%
```

As you can see, the info we get from the whois service is not always accurate.
