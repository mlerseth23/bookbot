import sys
from stats import lower_cases, total_words, letter_frequency #importing functions from 'stats.py'
# reads the content of a file and stores as variable file_contents
if len(sys.argv) == 1:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

def get_book_text(path_to_file):
	with open(path_to_file) as f:
		file_contents = f.read()
	return file_contents


def main(): #asks user for path to the file
	book = sys.argv[1]
	contents = get_book_text(book)
	result = lower_cases(contents)
	result1 = total_words(contents)
	
	print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
	print(f"Found {result1} total words")
	print("--------- Character Count -------")
	letter_frequency(result)
	print("============= END ===============")
print(sys.argv)

if __name__ == "__main__":
	main()
