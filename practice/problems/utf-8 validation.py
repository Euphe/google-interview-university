"""
https://leetcode.com/problems/utf-8-validation/#/description

A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:

For 1-byte character, the first bit is a 0, followed by its unicode code.
For n-bytes character, the first n-bits are all one's, the n+1 bit is 0, followed by n-1 bytes with most significant 2 bits being 10.
This is how the UTF-8 encoding would work:

   Char. number range  |        UTF-8 octet sequence
      (hexadecimal)    |              (binary)
   --------------------+---------------------------------------------
   0000 0000-0000 007F | 0xxxxxxx
   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
Given an array of integers representing the data, return whether it is a valid utf-8 encoding.

Note:
The input is an array of integers. Only the least significant 8 bits of each integer is used to store the data. This means each integer represents only 1 byte of data.

Example 1:

data = [197, 130, 1], which represents the octet sequence: 11000101 10000010 00000001.

Return true.
It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.
Example 2:

data = [235, 140, 4], which represented the octet sequence: 11101011 10001100 00000100.

Return false.
The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
The next byte is a continuation byte which starts with 10 and that's correct.
But the second continuation byte does not start with 10, so it is invalid.

"""
def get_char_byte_num(btext):
    if btext[0] == '0':
        return 0
    return btext.find('0')-1

def validate_leading_byte(btext):
    if btext[:2] == '10':
        return False
    if btext.find('0') == -1 or btext.find('0') > 4:
        return False
    return True

def validate_typical_byte(btext):
    return btext[:2] == '10'

def to_bin(x):
    bin_text = '{:b}'.format(x)
    diff = (8-len(bin_text))
    if diff < 0:
        diff = 0
    bin_text = diff*'0'+bin_text
    return bin_text
    
class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        if not data:
            return False
        bdata = [to_bin(x) for x in data ] 
        i=0
        #print(bdata)
        while i < len(bdata):
            byte = bdata[i]
            if not validate_leading_byte(byte):
                return False
            bytes_ahead = get_char_byte_num(byte)
            #print(byte, 'byte')
            #print(bytes_ahead, 'ahead')
            if bytes_ahead > 0:
                for j in range(1, bytes_ahead+1):
                    if i+j >= len(bdata):
                        return False
                    if not validate_typical_byte(bdata[i+j]):
                        return False
                i = i+bytes_ahead+1
            else:
                i = i +1
        
        return True

                   
           
           