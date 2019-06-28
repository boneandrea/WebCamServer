#!/bin/bash

## Script to notify ip address to MyDNS

DIR=$(dirname $(readlink -f $0))
cd $DIR

#MAILTO= # moved to .env

. ./.env

# TODO: if fail ( not 200 ) ??
wget -O - https://$ID:$PASS@ipv4.mydns.jp/login.html

exit
