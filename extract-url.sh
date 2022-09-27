#!/bin/sh
grep "^http" $1 | cut -d"," -f1 | sort
