from string                     import ascii_letters, digits

def forTwitter(string):
    TWITTER_ALLOWED_CHARS = frozenset(ascii_letters + digits + '-._~')
    if type(string) is not str:  
        string = str(string)
    encoded = ''
    for char in string:
        if char in TWITTER_ALLOWED_CHARS: 
            encoded += char
        else:
            # percent encode every byte in the unicode char 
            unicode_char = char.encode()
            for byte in unicode_char:
                encoded += ''.join(['%' + str(hex(int(byte)))[2:].upper()]) 
    return encoded
