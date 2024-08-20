def decode_message(encoded_message):
    def decode_inner(encoded):
        key = 3 
        decoded_chars = []
        
        for char in encoded:
            if char.isalpha():  
                shifted = ord(char) - key
                if char.islower():
                    if shifted < ord('a'):
                        shifted += 26
                elif char.isupper():
                    if shifted < ord('A'):
                        shifted += 26
                decoded_chars.append(chr(shifted))
            else:
                decoded_chars.append(char)
        
        return ''.join(decoded_chars)
    
    decoded_message = decode_inner(encoded_message)
    return decoded_message

def demonstrate_scope_with_decode():
    encoded_message = "Thao My!" 
    print(f"Encoded Message: {encoded_message}")
    
    decoded = decode_message(encoded_message)
    print(f"Decoded Message: {decoded}")
    
    try:
        print(f"Key used for decoding: {key}")
    except NameError as e:
        print(f"Error: {e} (This demonstrates scope and name resolution)")
    
    def encode_message(decoded_message):
        def encode_inner(decoded):
            key = 3 
            encoded_chars = []
            
            for char in decoded:
                if char.isalpha(): 
                    shifted = ord(char) + key
                    if char.islower():
                        if shifted > ord('z'):
                            shifted -= 26
                    elif char.isupper():
                        if shifted > ord('Z'):
                            shifted -= 26
                    encoded_chars.append(chr(shifted))
                else:
                    encoded_chars.append(char)
            
            return ''.join(encoded_chars)
        
        encoded_message = encode_inner(decoded_message)
        return encoded_message
    
    encoded_again = encode_message(decoded)
    print(f"Encoded Again: {encoded_again}")

if __name__ == "__main__":
    demonstrate_scope_with_decode()


    