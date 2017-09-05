def is_palindrome(text):
	if len(text) < 2:
		return False
	return text[:len(text)//2] == text[len(text)//2:][::-1]

def remove_palindromes(text):
	if not text or len(text) < 2:
		return text 

	out_text = text
	deletion = True
	while deletion: #Delete all adjacent pairs until none are present in string
		deletion = False
		for i in range(1, len(text)):
			if text[i] == text[i-1]:
				print('pair', text[i], text[i-1])
				out_text = out_text.replace(text[i]+text[i-1], '', 1)
				deletion = True

		if deletion:
			text = out_text

	return out_text

assert remove_palindromes('ww') ==  ''
assert remove_palindromes('wwst') ==  'st'
assert remove_palindromes('wwsttsww') ==  ''
assert remove_palindromes('wwstdaadierfflitzzz') ==  'stierlitz'