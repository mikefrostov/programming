#!/bin/bash

filename=logfile.log

function generate_logfile() {
  temp=$(date +%s)
  decrement=100000
  echo "generating logfile $filename"
  for i in {1..100}
  do
    temp=$(($temp-$decrement))
    date -d @$temp '+%Y-%m-%d' >> $filename
  done
  echo "done"
}

function cut_logfile() {
    echo "deleting logs from a logfle older than 7 days"    
}

#prin_logfile()

function main {
    echo "You have started the bash solution"
    echo "Written by Mikhail Morozov"
    generate_logfile
    cut_logfile
}

main
