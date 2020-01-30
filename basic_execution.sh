#!/bin/bash

if [[ -z $1 ]]; then
  gcc caesar.c -o caesar.out -w

  ./caesar.out textfiles/aohf.txt textfiles/aohf_ct3.txt e 3
  ./caesar.out textfiles/pap.txt textfiles/pap_ct7.txt e 7

  for i in $(ls textfiles); do
    python charcount.py -i textfiles/$i -o csvfiles/"$(basename "$i" .txt).csv"
  done
elif [[ $1 == "-c" ]]; then
  # Clean up
  rm caesar.out
  rm textfiles/aohf_ct3.txt textfiles/pap_ct7.txt
  rm csvfiles/*
fi
