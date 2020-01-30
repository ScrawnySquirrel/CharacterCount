import argparse
import numpy as np

# Define script description and the arugment list
parser = argparse.ArgumentParser(description='Get a count of all English letters and calculate the relative distribution.')
parser.add_argument('-p', '--ptfile', help='name of the plaintext file', required=True)
parser.add_argument('-c', '--ctfile', help='name of the ciphertext file', required=True)
parser.add_argument('-m', '--msg', help='the plaintext character to calculate conditional probability', required=True)
parser.add_argument('-o', '--out', help='name of the output CSV file')
args = parser.parse_args()

# Open plaintext and ciphertext files to read
pt_f = open(args.ptfile, "r")
ct_f = open(args.ctfile, "r")

orig_msg = ""

# Skip first lines
next(pt_f)
next(ct_f)

# Find the line with the plaintext charater, remove trailing whitespace, and store into array
for line in pt_f:
    if args.msg in line:
        orig_msg = line.rstrip().split(',')
        break

# print(orig_msg)

# Loop through ciphertext file and calculate the condition probability
prob_min = 12345
min_line = []
for line in ct_f:
    ct = line.split(',')
    condprob = float(orig_msg[2])/float(ct[2])
    print("P(M={}|C={}) = {}".format(orig_msg[0], ct[0], condprob))
    # Get the value closest to 1 (100%)
    if abs(condprob-1) < prob_min:
        prob_min = abs(condprob-1)
        min_line = line

# Calculte distance of plaintext char and the matched ciphertext
dist = abs(ord(orig_msg[0]) - ord(min_line[0]))

print("Character {} is mapped to {} with the distance of {}".format(orig_msg[0], min_line[0], dist))
