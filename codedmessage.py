import random
import string


def randomchar():
  return ''.join(random.choice(string.ascii_letters) for i in range(3))


def encrypt(message):
  if len(message) >= 3:
    value = message[0]
    message = message[1:len(message)] + value
    message = message[::-1]
    result = randomchar() + message + randomchar()
    print(result)
  else:
    message = message[::-1]
    print(message)

def decrypt(message):
  if len(message) >= 3:
    message = message[3:len(message) - 3]
    message = message[::-1]
    value = message[-1]
    message = value + message[0:len(message)-1]
    print(message)
  else:
    message = message[::-1]
    print(message)

while True:
  choice = input("Enter 'E' for encryption and 'D' for decryption: ").lower()
  user_string = input("Enter message: ")
  value = 0
  if choice == 'e':
    encrypt(user_string)
  elif choice == 'd':
    decrypt(user_string)
  else:
    raise ValueError("Invalid choice")
