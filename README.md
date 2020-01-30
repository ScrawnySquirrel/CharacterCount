# CharacterCount and ConditionalProbability

CharacterCount > Application for counting occurrences of letters in a text file and calculating the relative distribution
ConditionalProbability > Application for calculating the conditional probability P(M=m|C=c).

## Getting Started

These instruction will help generate CSV files with count and relative distribution of each letter in the English alphabet. Furthermore, it will help guide using the generated CSV file to calculate the conditional probability.

## Prerequisite

* Python2

## Getting relative distribution and conditional probability

There are 2 main files: `charcount.py` and `condprob.py`.
* `charcount.py` will get a count of letter and calculate the relative distribution
* `condprob.py` will calculate the conditional probability and the Caesar key.

### Count letter frequency and relative distribution

The `charcount.py` will perform the logic to count the character frequency of each letter in the English language. Please note, the script will default all characters to be their lowercase equivalent.

```
python charcount.py -i textfiles/aohf.txt -o csvfiles/aohf.csv
```
Using the script is very simple. The only required argument is the `-i`. The passed argument must be a text file.

`-o` flag is optional and if it is not defined, the result will be outputted to stdout.

### Calculate the conditional probability

The `condprob.py` will perform the logic to calculate the conditional probability based on the plaintext CSV, ciphertext CSV, and the letter to match.

```
python condprob.py -p csvfiles/aohf.csv -c csvfiles/aohf_ct3.csv -m e -o csvfiles/aohf_condprob.csv
```
Similar to `charcount.py`, the `-o` flag is option and will display result to stdout if not defined.

## Running the tests

All the test data and results are provided in the `textfiles` folder. It contains 2 books:
* Adventures of Huckleberry Finn By Mark Twain
* Pride and Prejudice by Jane Austen

For simplicity, a bash script is provided to get the relative distribution and conditional probability called `basic_execution.sh`.

This script will use the provided `caesar.c` to generate the ciphertext file that will be stored in `textfiles` with `*_ct#.text` format based on the plaintext files in `textfiles`.

When the ciphertext is generated, the script will generate CSV with character count and relative distribution using `charcount.py`.

Afterwards, the genereated CSV from `charcount.py` will be used to calculate the the conditional probabilty and output the result as `*_condprob.csv`.

> The generated CSVs will be stored in the `csvfiles` directory.

## Author

**Gabriel Lee** - [ScrawnySquirrel](https://github.com/ScrawnySquirrel)
