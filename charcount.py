import argparse

# Define script description and the arugment list
parser = argparse.ArgumentParser(description='Get a count of all English letters and calculate the relative distribution.')
parser.add_argument('-i', '--input', help='name of the input text file')
parser.add_argument('-o', '--output', help='name of the output CSV file')
args = parser.parse_args()
