#!/bin/bash

if [[ -z $1 ]]; then
  # Create caesar.c executable
  gcc caesar.c -o caesar.out -w

  # Generated ciphertext
  ./caesar.out textfiles/aohf.txt textfiles/aohf_ct3.txt e 3
<<<<<<< HEAD
  ./caesar.out textfiles/pap.txt textfiles/pap_ct5.txt e 5
=======
  ./caesar.out textfiles/pap.txt textfiles/pap_ct7.txt e 5
>>>>>>> 6e2bd82c061d41997fd5cf70e0e51489565a506a

  # Get character count and distribution
  mkdir csvfiles
  for i in $(ls textfiles); do
    python charcount.py -i textfiles/$i -o csvfiles/"$(basename "$i" .txt).csv"
  done

  for j in {e,t,a,o,i,n}; do
    echo "Letter: $j" >> csvfiles/aohf_condprob.csv
    python condprob.py -p csvfiles/aohf.csv -c csvfiles/aohf_ct3.csv -m $j -o csvfiles/aohf_condprob.csv
    python condprob.py -p csvfiles/pap.csv -c csvfiles/pap_ct5.csv -m $j -o csvfiles/pap_condprob.csv
  done
elif [[ $1 == "-c" ]]; then
  # Clean up
  rm caesar.out
  rm textfiles/aohf_ct3.txt textfiles/pap_ct7.txt
  rm csvfiles/*
fi
