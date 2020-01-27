import argparse

# Define script description and the arugment list
parser = argparse.ArgumentParser(description='Get a count of all English letters and calculate the relative distribution.')
parser.add_argument('-i', '--input', help='name of the input text file', required=True)
parser.add_argument('-o', '--output', help='name of the output CSV file')
args = parser.parse_args()

# Read input file
in_f = open(args.input, "r")

# Create output file
if args.output is not None:
    out_f = open(args.output, "w")
else:
    out_f = open("charcount.csv", "w")
out_f.write("letter,count,probability\n")

contents = in_f.read().lower()
eng_alpha = "abcdefghijklmnopqrstuvwxyz"
char_dict = {}
char_count = 0

for chr in eng_alpha:
    char_dict[chr] = contents.count(chr)
    char_count += char_dict[chr]

rel_prob_sum = 0

for chr in eng_alpha:
    rel_prob = float(char_dict[chr])/float(char_count)
    out_f.write("{},{},{}\n".format(chr,char_dict[chr], rel_prob))
    rel_prob_sum += rel_prob

print(rel_prob_sum)

# print(char_dict)
# print(char_count)
