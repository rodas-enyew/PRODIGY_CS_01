 # Caesar Cipher

import pyperclip
def caesar_cipher(text, key, mode):
  SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.`~@#$%^&*()_+-=[]{}|;:<>,/'
  translated=''

  for symbol in text:
    if symbol in SYMBOLS:
       symbolIndex = SYMBOLS.find(symbol)


       if mode == 'encrypt':
           translatedIndex = symbolIndex + key #The	index	returned	by	the	find()	call	is	stored	in symbolIndex.
       elif mode == 'decrypt':
          translatedIndex = symbolIndex - key
 # Handle wraparound, if needed:
       if translatedIndex >= len(SYMBOLS):
          translatedIndex = translatedIndex - len(SYMBOLS)
       elif translatedIndex < 0:
          translatedIndex = translatedIndex + len(SYMBOLS)

       translated = translated + SYMBOLS[translatedIndex]
    else:
       translated= translated + symbol
       
  return translated


#user input
message = input("Enter your message: ")
key = int(input("Enter key value: "))
mode = input("Enter mode(encrypt/decrypt): ").lower()


translated = caesar_cipher(message, key, mode)

#output result with proper lable
if mode == 'encrypt':
  print(f"Encrypted: {translated}")
elif mode == 'decrypt':
  print(f"Decrypted: {translated}")
else:
  print("Invalid mode! Please enter 'encrypt' or 'decrypt'.")

 # Output the translated string:

pyperclip.copy(translated)
