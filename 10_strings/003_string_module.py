#  IMPORTING THE STRING MODULE AND EXPLORING CONSTANTS
import string
 
print(string.ascii_letters)        
# Output: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
 
print(string.ascii_lowercase)      
# Output: abcdefghijklmnopqrstuvwxyz
 
print(string.ascii_uppercase)      
# Output: ABCDEFGHIJKLMNOPQRSTUVWXYZ
 
print(string.digits)               
# Output: 0123456789
 
print(string.hexdigits)            
# Output: 0123456789abcdefABCDEF
 
print(string.punctuation)          
# Output: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
 



#  can print all the alphabets using a loop
for ch in string.ascii_lowercase:
    print(ch, end=" ")