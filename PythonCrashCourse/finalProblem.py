def caught_speeding(speed, is_birthday):
	if is_birthday:
		if speed <= 65:
			print('He is clear. Let him go !!')
		elif speed>66 and speed<=85:
			print("He's Guilty. Charge him Small Ticket !!")
		else:
			print("He's Guilty. CHarge him Big Ticket !!")
	else:
		if speed <= 60:
			print('He is clear. Let him go !!')
		elif speed>61 and speed <= 80:
			print("He's Guilty. Charge him Small Ticket !!")
		else:
			print("He's Guilty. CHarge him Big Ticket !!")


print("How fast was he going?")
speed = int(input("Km/hr: "))

print("Ask when is his Birthday. If it's Today, write yes else, write no.")
value = input("yes/no: ")
birthday = False
if value == 'yes':
	birthday = True

caught_speeding(speed, birthday)
