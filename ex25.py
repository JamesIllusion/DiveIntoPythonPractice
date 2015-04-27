def break_word(stuff):
	"""This funciton will break up words for you"""
	words = stuff.split(' ')
	return words

def sort_word(words):
	"""Sort the words"""
	return sorted(words)

def print_first_word(words):
	"""Print the first word after popping it off"""
	word = words.pop(0)
	print word

def print_last_word(words):
	"""Print the last word after popping it off"""
	word = words.pop(-1)
	print word

def sort_sentence(sentence):
	"""Takes a full sentence and returns the sorted words"""
	words = break_word(sentence)
	return sort_word(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)
