import hashlib

def convert_text_to_sha1(password):
    digest = hashlib.sha1(password.encode()).hexdigest()

    return digest

def main():
    user_sha1 = input("Enter the SHA1 to crack: ")
    clean_user_input = user_sha1.strip().lower()

    with open("./passwords.txt") as f:
        for line in f:
            password = line.strip()
            converted_sha1 = convert_text_to_sha1(password)

            if clean_user_input == converted_sha1:
                print(f"Password Found: {password}")
                return

    print("No matching password")                

if __name__ == "__main__":
    main()