import math
import re

status =''
S = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
l = len(S)

#Functions

def hack_caesar_cipher (msg, l, S):
	for k in range(l): # In this case, 66 iterations => 66 possible 
		msg_encypted = ''
		c = ''
		for c in msg:
			if c in S: # Only characters in 'S' 
				c_index = S.index(c) # Character's index

				c_dec_index = (c_index - k)% l

				msg_encypted += S[c_dec_index] 
			else :
				msg_encypted += c 
		print("# %s => %s " %(k, msg_encypted))
		# return msg_encypted

#Main

def Main():

	msg = input('Please Enter your Message to Decrypt :')
	print('Your Decrypted Message is : ', msg)
	print('\n')
	print('Processing now ...' )
	hack_caesar_cipher(msg, l, S)
	
if __name__ == '__main__':
 	Main()