# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1=str(name1)
name2=str(name2)

name=name1+name2

name=name.lower()

a=str(name.count('t')+name.count('u')+name.count('r')+name.count('e'))

b=str(name.count('l')+name.count('o')+name.count('v')+name.count('e'))



if 90<int(a+b):
  print(f'Your scores {a+b}, you go together like coke and mentos')
elif 10>int(a+b):
  print(f'Your scores {a+b}, you go together like coke and mentos')
elif 40<int(a+b):
  
  if 90<int(a+b):
    print(f'Your scores {a+b}, you go together like coke and mentos')
  elif 50>int(a+b):
    print(f'Your scores {a+b}, you are alright together')
  else:
    print(f'Your score is {a+b}')


else:
  print(f'Your score is {a+b}')




