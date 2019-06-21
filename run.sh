#!/bin/bash

cd `dirname $0`

. ./v2/bin/activate
python srv.py
