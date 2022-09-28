#!/bin/sh
echo $(echo $1 | grep -oE '([a-z][[a-z]).csv'),`grep "^http://" $1 | wc -l`,`grep "^https://" $1 | wc -l`
