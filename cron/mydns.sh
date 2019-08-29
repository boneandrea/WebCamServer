#!/bin/bash

## Script to notify ip address to MyDNS

TMP=$(mktemp)
atexit() {
  [[ -n ${TMP-} ]] && rm -f "$TMP"
}

trap atexit EXIT
trap 'rc=$?; trap - EXIT; atexit; exit $?' INT PIPE TERM

DIR=$(dirname $(readlink -f $0))
cd $DIR

#MAILTO= # moved to .env

. ./.env || exit 1

# TODO: if fail ( not 200 ) ??
wget -O $TMP "http://www.mydns.jp/directip.html?MID=${ID}&PWD=${PASS}&IPV4ADDR=${IPADDR}"

grep -q "Login and IP address notify OK" $TMP

if [ $? = 0 ] ; then
	EXIT=0
else
	#echo | mail -s "mydns update failed" $MAILTO
	EXIT=1
fi

exit $EXIT
