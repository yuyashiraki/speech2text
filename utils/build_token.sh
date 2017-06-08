#!/bin/sh
gcloud auth application-default login
gcloud auth application-default print-access-token > .token
