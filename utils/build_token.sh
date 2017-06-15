#!/bin/sh
cd `dirname $0`
gcloud auth application-default login
gcloud auth application-default print-access-token > $PWD/../TOKEN
