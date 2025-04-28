import random

def generate_password(length, chars):
   password = ''.join(random.choice(chars) for x in range(length))
   return password

# Example usage
password = generate_password(8, "abcde")
print(f"Generated password: {password}")