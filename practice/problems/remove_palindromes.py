
# def remove_palindromes(text):
# 	if not text or len(text) < 2:
# 		return text 

# 	out_text = text
# 	deletion = True
# 	while deletion: #Delete all adjacent pairs until none are present in string
# 		deletion = False
# 		for i in range(1, len(text)):
# 			if text[i] == text[i-1]:
# 				out_text = out_text.replace(text[i]+text[i-1], '', 1)
# 				deletion = True

# 		if deletion:
# 			text = out_text

# 	return out_text

def get_palindrome_bounds(text, palindrome_index):
	left = palindrome_index
	right = palindrome_index+1
	while (text[left] == text[right]): #move outwards until we reach the end/start of string or the string between left and right stops being a palindrome 
		if left -1 >= 0 and right+1 < len(text) and text[left-1] == text[right+1]: 
			left = left-1
			right = right + 1
		else:
			break
	return left, right

def remove_even_palindromes(text):
	if not text or len(text) < 2:
		return text 

	left = 0
	right = 1

	out_text = ''
	while right < len(text): #Find adjacent pair, get palindrome that contains it, add everything before it to out, proceed after the palindrome
		if text[right-1] == text[right]: #Found a pair
			palindrome_left_bound, palindrome_right_bound = get_palindrome_bounds(text, right-1)
			out_text+= text[left:palindrome_left_bound]
			left = palindrome_right_bound+1
			right = left
		right+=1
	out_text+= text[left:]
	return out_text

assert remove_even_palindromes('ww') ==  ''
assert remove_even_palindromes('www') == 'w'
assert remove_even_palindromes('ztwwst') ==  'ztst'
assert remove_even_palindromes('wwsttsww') ==  ''
assert remove_even_palindromes('wwstdaadi') ==  'sti'
assert remove_even_palindromes('wwstdaadierfflitzzz') ==  'stierlitz'