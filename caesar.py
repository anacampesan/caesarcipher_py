def encode(message, key):
	chars = []
	message = message.lower()
	for m in message:
		chars.append((ord(m)+key))
	return chars
	
def decode(message, key):
	decoded = []
	for m in message:
		#for last letters of the aphabet
		if m in range(120, 122):
			decoded.append(chr(m-22+key))
		else:
			decoded.append(chr(m-key))
	#returning the array altogether
	return "".join(decoded)

