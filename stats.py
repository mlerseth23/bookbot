def total_words(book): #get total words from a book
	book_split = book.split()
	num_words = len(book_split)
	return num_words

def lower_cases(book):
	lower_book = book.lower()
	frankenstein_dictionary = {} #creating dictionary
	for char in lower_book:
		if char.isalpha():
			if char in frankenstein_dictionary:
				frankenstein_dictionary[char] += 1
			else:
				frankenstein_dictionary[char] = 1
	return frankenstein_dictionary

def letter_frequency(book):
	sorted_items = sorted(book.items(), key=lambda item: item[1], reverse=True)
	sorted_items = {key: value for key, value in sorted_items}
	for key, value in sorted_items.items():
		print(f"{key}: {value}")
	return