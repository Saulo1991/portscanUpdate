import hashlib

def convert_text_to_sha1(text):
    digest = hashlib.sha1(
        text.encode()
    ).hexdigest()
    
    return digest

def main():
    user_sha1 = input('Enter the SHA1 to assess: ')
    cleaned_user_sha1 = user_sha1.strip().lower()
    
    with open('./passwords.txt') as pw:
        for line in pw:
            password = line.strip()
            converted_sha1 = convert_text_to_sha1(
                password
                )
            
            if cleaned_user_sha1 == converted_sha1:
                print(f'Password Found: {password}')
                return
            
    print('Could not find the password')

if __name__ == '__main__':
    main()