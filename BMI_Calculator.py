# ********************** BMI Calculator *************************

# Project Idea: have the user input their weight in lbs or kg (the program can convert it to lbs)
# and height in ft/inches or cms (the program can convert it to ft/inches). Then calculate his/her
# BMI and print the message and direct them to the corresponding links for some safe fitness tips
# This project practices webbrowser.open and try/except error catch

import sys
import webbrowser
# https://docs.python.org/3/library/webbrowser.html
# webbrowser.open(url, new=0, autoraise=True)
# Display url using the default browser. If new is 0, the url is opened in the same browser window if possible.
# If new is 1, a new browser window is opened if possible. If new is 2, a new tab is opened if possible.
# If autoraise is True, the window is raised if possible (note that under many window managers this will occur
# regardless of the setting of this variable).

def calculate_BMI():
	bmi = 0
	# embed link to convert weight
	print('Clik here to convert pound to kg:',
		  (webbrowser.open("https://www.unitconverters.net/weight-and-mass/lbs-to-kg.htm", new = 1, autoraise = True)))
	weight = float(input('Please enter your weight in kg: '))
	# exit program gracefully
	if weight <= 0:
		print('Invalid weight. Try again or press n/N/No/NO to quit: ')
		try:
			weight = float(input())
		except ValueError:
			sys.exit()

	else:
		# pass
		# embed link to convert weight
		print('Clik here to convert ft to cm:',
			  (webbrowser.open("https://www.rapidtables.com/convert/length/feet-to-cm.html", new = 1, autoraise = True)))
		height = float(input('Please enter your height in cm: '))
		# exit program gracefully
		if height <= 0 or height > 250:
			print('Invalid height. Try again or press n/N/No/NO to quit: ')
			try:
				height = float(input())
			except ValueError:
				sys.exit()

			# now we have both weight and height info, we can calculate the bmi
		else:
			height = height / 100
			bmi = weight / (height ** 2)

		# print BMI
	print('Your Body Mass Index (BMI) is:', round(bmi, 1))

	# mapping BMI to message and corresponding fitness links
	if bmi <= 18.5:
		print('You are underweight.' '\n')
		print('Check here for tips to safely gain weight:', webbrowser.open("https://www.healthline.com/nutrition/how-to-gain-weight"))
	elif bmi > 18.5 and bmi <= 24.9:
		print('You are normal weight.')
	elif bmi > 25 and bmi <= 29.9:
		print('You are overweight.' '\n')
		print('Check here for tips to safely lose weight:', webbrowser.open("https://www.medicalnewstoday.com/articles/324123"))
	elif bmi >= 30:
		print('Obesity')
		print('Check here for tips to safely lose weight:', webbrowser.open("https://www.medicalnewstoday.com/articles/324123"))

def main():
	calculate_BMI()

if __name__ == '__main__':
	main()
