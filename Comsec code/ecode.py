

# Run the code using : python ecode.py

# Mapping functions 
# Converts an uppercase letter ( A to Z ) to a number ( 0 to 25)
def letter_to_number(letter):
    return ord(letter) - ord('A')


# Converts a number ( 0 to 25 ) back to its respective uppercase letter ( A to Z )
def number_to_letter(number):
    return chr(number + ord('A'))


# Encryption function


def encrypt(plaintext, key):
    # Remove spaces and convert everything to uppercase for consistency
    plaintext = plaintext.replace(" ", "").upper()
    key = key.replace(" ", "").upper()
   
    # Check if the key is long enough; if not, raise an error
    if len(key) < len(plaintext):
        raise ValueError("Key must be at least as long as the plaintext.")
   
    # Trim the key to match the length of the plaintext
    key = key[:len(plaintext)]
    cipher = ""  # Initialize an empty string to build the ciphertext


    # Encrypt each character 
    for p_char, k_char in zip(plaintext, key):
        # Convert plaintext and key characters to numbers 0 to 25
        p_num = letter_to_number(p_char)
        k_num = letter_to_number(k_char)


        # Add the numbers then mod 26
        c_num = (p_num + k_num) % 26


        # Convert the result back to a letter and append to the ciphertext
        cipher += number_to_letter(c_num)


    return cipher  # Return the fully encrypted ciphertext


# User Input Section 


# Ask user to enter the plaintext
plaintext = input("Enter plaintext (A to Z only, no punctuation): ")


# Ask user to enter the key ,must be at least as long as the plaintext
key = input("Enter key (A to Z only, must be >= length of plaintext): ")


# Try to encrypt the plaintext using the given key
try:
    cipher_text = encrypt(plaintext, key)  # Encrypt the input


    # Display the the instructions & results
    print("\n--- Encryption Output ---")
    print("Plaintext:", plaintext.upper())
    print("Key used: ", key[:len(plaintext)].upper())
    print("Ciphertext:", cipher_text)


# If there's an error (like key being too short), print the error message
except ValueError as ve:
    print("Error:", ve)