import os
import json
import yaml
import schema
import helper
import requester

print('+-----------------------------------+\n| Welcome to Spring Snake CLI Client |\n+-----------------------------------+\n'+helper.nice_image+'''
Hello there, welcome to Spring Snake, a code that allows you to save and retrieve some key-value data with Python and Spring Boot APIs.
Please, tell me, what do you want to do?:
1) I want to save some data
2) I want to get some data
3) I want to delete some data''')
option = input()
response = 'y'
while response != 'n':
  while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    if option == '1':
      keys = []
      values = []
      while True:
        print("Now insert the key of the value you want to save:")
        key = input()
        print("Nice! Now, insert the value you want to save:")
        value = input()
        if (not key) or (not value):
          print("Sorry, I didn't understand that. Please, try again.")
        else:
          print("Good! Now, do you want to save more values? (y/n)")
          response = input()
          if response != 'y' and keys.lenght() == 0:
            requester.save(key, value)
            break
          else:
            keys.add(key)
            values.add(value)
          if response != 'y' and keys.lenght() != 0:
            break
        if keys.lenght() == 0:
          break
        else:
          requester.saveall(keys, values)
      break
    elif option == '2':
      print("Do you want to get a specific value or all values? (s/a)\n")
      response = input()
      if response == 's':
        print("Now, insert the key you want to get:")
        key = input()
        print('The linked value is: ' + requester.get(key))
      elif response == 'a':
        print('Do you want to get all of them here or in a file? (h/f)')
        response = input()
        if response == 'h':
          print(requester.getall().toString())
        elif response == 'f':
          print('Nice! Now, do you prefer to have them in a JSON format or a YAML format? (j/y)')
          response = input()
          if response == 'j':
            with open("output.json", "w") as outfile:
              outfile.write(requester.getall())
          elif response == 'y':
            with open("output.yaml", "w") as outfile:
              outfile.write(yaml.dump(requester.getall()))
        else:
          print("Sorry, I didn't understand that. Please, try again.")
      else:
        print("Sorry, I didn't understand that. Please, try again.")
    elif option == '3':
      print("Do you want to delete just one value or all of them? (o/a)")
      response = input()
      if response == 'o':
        print("Now, insert the key of the value you want to delete:")
        key = input()
        requester.delete(key)
      elif response == 'a':
        print("Are you sure? (y/n)")
        response = input()
        if response == 'y':
          requester.deleteall()
        elif response == 'n':
          print("Ok, then.")
        else:
          print("Sorry, I didn't understand that. Please, try again.")
      else:
        print("Sorry, I didn't understand that. Please, try again.")
    break
  print("Do you want to do something else? (y/n)")
  response = input()
  if response != 'n':
    print('''Now please, tell me, what do you want to do?:
    1) I want to save some data
    2) I want to get some data
    3) I want to delete some data''')
    option = input()
  os.system('cls' if os.name == 'nt' else 'clear')