#!/bin/bash

## Script to notify ip address to MyDNS

DIR=$(dirname $(readlink -f $0))
cd $DIR

MAILTO=bone.andrea.anthrax@gmail.com

. ./.env

wget -O - https://$ID:$PASS@ipv4.mydns.jp/login.html

exit
