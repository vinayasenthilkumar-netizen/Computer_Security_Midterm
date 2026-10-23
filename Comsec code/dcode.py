
# run code like this : python dcode.py

#  Mapping functions
# Convert an uppercase letter (A to Z) to a number (0 to 25)
def letter_to_number(letter):
    return ord(letter) - ord('A')


# Convert a number (0 to 25) back to an uppercase letter (A to Z)
def number_to_letter(number):
    return chr(number + ord('A'))


#  Decryption function


def decrypt(ciphertext, key):
    # Remove spaces and convert both the ciphertext and the key to uppercase
    ciphertext = ciphertext.replace(" ", "").upper()
    key = key.replace(" ", "").upper()


    # Ensure the key is at least as long as the ciphertext else error
    if len(key) < len(ciphertext):
        raise ValueError("Key must be at least as long as the ciphertext.")


    # Trim the key to match the length of the ciphertext exactly
    key = key[:len(ciphertext)]
    plaintext = ""  # Initialize an empty string for the decrypted message


    # Decrypt each letter
    for c_char, k_char in zip(ciphertext, key):
        c_num = letter_to_number(c_char)  # Convert ciphertext letter to number
        k_num = letter_to_number(k_char)  # Convert key letter to number


        # Subtract key number from ciphertext number, add 26 to avoid negative then mod 26 it
        p_num = (c_num - k_num + 26) % 26


        # Convert the result number back to a letter and append to plaintext
        plaintext += number_to_letter(p_num)


    # Return the decrypted plaintext, cleaned ciphertext, and trimmed key
    return plaintext, ciphertext, key


# Main Program 


try:
    # Take user input for ciphertext and key, allowing spaces for readability
    ciphertext_input = input("Enter ciphertext (A to Z only, spaces allowed): ")
    key_input = input("Enter key (must be >= length of ciphertext, spaces allowed): ")


    # Perform decryption using the provided inputs
    plaintext_result, clean_ciphertext, trimmed_key = decrypt(ciphertext_input, key_input)


    # Display original inputs and the decryption result clearly
    print("\n--- Decryption Output ---")
    print("Original Ciphertext : ", ciphertext_input)
    print("Cleaned Ciphertext  : ", clean_ciphertext)
    print("Key used            : ", trimmed_key)
    print("Decrypted Plaintext : ", plaintext_result)


except ValueError as ve:
    # Handle errors such as key length issues gracefully by printing the error message
    print("Error:", ve)
