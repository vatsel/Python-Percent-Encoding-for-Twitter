def forTwitter(string):
    '''percent encodes everything except alphanumerics and 4 twitter specific chars'''
    twitterAllowedChars = set([48,49,50,51,52,53,54,55,56,57, #numbers decimal encoding
                          65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90, #uppercase
                          97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122, #lowercase
                          45,46,95,125 #dash,dot,underscore,tilde                         
                          ])
    if type(string) is not str: raise TypeError("string expected, received type "+str(type(string)))
    encoded = ''
    for char in string:
        ordinal = ord(char)
        if ordinal in twitterAllowedChars: encoded += char
        else: encoded += '%'+hex(ordinal)[2:] #replace 0x prefix with %
    return encoded
        
