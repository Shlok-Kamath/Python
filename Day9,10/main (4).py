#Write your code below this line 👇



def prime_checker(number):
	prime=True

	if number==1:
		print('Its neither prime nor composite')
	
	elif number<=0:
		print('Only natural numbers can be prime or composite')
	else :

		for a in range(2,number):
			if number%a==0:
				prime=False
		
		if prime==False :
			print("It's not a prime number.")
		else :
			print("It's a prime number.")




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



