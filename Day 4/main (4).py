# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

#a=str(input('write column number- '))
#b=str(input('write row number- '))

if position=='11':
  row1[0]='x'
elif position=='21':
  row1[1]='x'
elif position=='31':
  row1[2]='x'
elif position=='12':
  row2[0]='x'
elif position=='22':
  row2[1]='x'
elif position=='32':
  row2[2]='x'  
elif position=='13':
  row3[0]='x'
elif position=='23':
  row3[1]='x'
elif position=='33':
  row3[2]='x'  







#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")