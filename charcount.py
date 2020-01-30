import argparse

# Define script description and the arugment list
parser = argparse.ArgumentParser(description='Get a count of all English letters and calculate the relative distribution.')
parser.add_argument('-i', '--input', help='name of the input text file', required=True)
parser.add_argument('-o', '--output', help='name of the output CSV file')
args = parser.parse_args()

# Read input text file
in_f = open(args.input, "r")

# Create output CSV file
if args.output is not None:
    out_f = open(args.output, "w")
else:
    out_f = open("charcount.csv", "w")

out_f.write("letter,count,probability\n")
contents = in_f.read().lower()

# Set global variables
eng_alpha = "abcdefghijklmnopqrstuvwxyz"
char_dict = {}
char_count = 0
rel_prob_sum = 0

# Get each character count and calculate max char_count
for chr in eng_alpha:
    char_dict[chr] = contents.count(chr)
    char_count += char_dict[chr]

print("Dictionary:\nletter\tcount\tdistribution")
# Calculate relative distribution and output data to CSV
for chr in eng_alpha:
    rel_prob = float(char_dict[chr])/float(char_count)
    out_f.write("{},{},{}\n".format(chr,char_dict[chr], rel_prob))
    print("{}\t{}\t{}".format(chr,char_dict[chr],rel_prob))
    rel_prob_sum += rel_prob

print("Relative Probability: {}".format(rel_prob_sum))
print("Character Count: {}".format(char_count))
