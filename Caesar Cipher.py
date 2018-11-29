print("WELCOME TO CIPHER SOFT ")

#Defining alphabets
Alphabets = {}
i = 1
for _ in range(97,123):
    
    Alphabets[str(chr(_))] = i
    i += 1
    
#defining functions for asking key

def ask_key():
    while True:

        try:
            keyin = int(input("Enter the key for coding/decoding : \t "))
        except:
            print("Please enter a valid number")
            continue
        else:
            break
    return keyin

#defining functions for enc or dec
def enc_or_dec():
    val = ''
    while True:
        
        try:
            val = input("Which service do you want? \n [A] Encoding \n [B] Decoding \n Enter the option as either A or B \t")
            val = val.lower()
        except:
            print("Please enter only A or B")
            continue
        else:
            if val=='a':
                serv = 1
                break
            elif val == 'b':
                serv = 0
                break
            else:
                continue
    return serv


#defining function for input of text
def enc_in():
    text = input("Please enter the statement to be encoded : \t")
    return text

def dec_in():
    text = input("Please enter the statement to be decoded : \t")
    return text

#defining class for encoding function based on the key    
class encode:
    
    def __init__(self, text, key = 1):
        self.key = key
        self.text = text
    
    def encode_msg(self):
        words = self.text.split()
        new_words = []
        new_word = []
        
        for _ in range(len(words)):
            
            letters = list(words[_])
            newletters = []
            
            for l in range(len(letters)):
                if 96<ord(letters[l].lower())<122:
                    numval = Alphabets[letters[l].lower()]
                    newval = numval + self.key
                    while True:
                        if newval > 26:
                            newval -= 26
                            continue
                        else:
                            break
                    toadd = chr(96+newval)
                else:
                    toadd = letters[l]
                    
                newletters.append(toadd)
                
            new_words.append("".join(newletters))
        
        for _ in range(len(new_words)):
            new_word.append(new_words[_].title())
        
        
        encoded = "\t".join(new_word)
        
        return encoded
        
            
class decode:
    
    def __init__(self,text,key):
        self.text = text
        self.key = key
    
    def decode_msg(self):
        words = self.text.split()
        new_words = []
        new_word = []
        
        for _ in range(len(words)):
            
            letters = list(words[_])
            newletters = []
            
            for l in range(len(letters)):
                if 96<ord(letters[l].lower())<122:
                    numval = Alphabets[letters[l].lower()]
                    newval = numval - self.key
                    while True:
                        if newval > 26:
                            newval -= 26
                            continue
                        elif newval <=0:
                            newval += 26
                            continue
                        else:
                            break
                    toadd = chr(96+newval)
                else:
                    toadd = letters[l]
                    
                newletters.append(toadd)
                
            new_words.append("".join(newletters))
        
        for _ in range(len(new_words)):
            new_word.append(new_words[_].title())
        
        
        decoded = "\t".join(new_word)
        
        return decoded
thehell = True  
while thehell:

    Opt = enc_or_dec()

    if Opt == 1:
        print("You have chosen to encode a message")
        intxt = enc_in()
        inkey = ask_key()

        encoding = encode(intxt,inkey)

        encoded_message = encoding.encode_msg()

        print("Here is the message that is encoded :\t {}".format(encoded_message))

        print("Thank you!")

        while True:
            try:
                anss = int(input("Would you like to try our service again ? \n 1. Yes \n 2. No \n Please enter the number as option"))
            except:
                print("Please enter either 1 or 2 \t")
                continue
            else:
                break
        if anss == 1:
            thehell = True
        else:
            thehell = False

    elif Opt == 0:
        
        print("You have chosen to denode a message")
        intxt = dec_in()
        inkey = ask_key()

        decoding = decode(intxt,inkey)

        decoded_message = decoding.decode_msg()

        print("Here is the message that is decoded :\t {}".format(decoded_message))

        print("Thank you!")

        while True:
            try:
                anss = int(input("Would you like to try our service again ? \n 1. Yes \n 2. No \n Please enter the number as option"))
            except:
                print("Please enter either 1 or 2 \t")
                continue
            else:
                break
        if anss == 1:
            thehell = True
        else:
            thehell = False
    else:
        print("Enter a valid number")
    
        
    