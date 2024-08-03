#BAND NAME GENERATOR
import random

answers = ["What word best captures the essence of your personal philosophy or belief system? ",
"If you could embody a concept or abstract idea, what would it be? ",
"What is a powerful metaphor that resonates with you and your experiences? ",
"What historical or cultural figure do you find most compelling, and why? ",
"What is a recurring dream or vision that has had a significant impact on you? ",
"How would you describe the emotional landscape of your life right now? ",
"What is a profound lesson you’ve learned from a challenge or hardship? ",
"What natural element or phenomenon do you feel a deep connection with? ",
"If you could choose a symbol that represents your core identity, what would it be? ",
"What phrase or saying do you believe captures the spirit of your creative vision? ",
"What's the name of the city you grew up in? ",
"What is the name of a pet? ",
"What's the name of your favorite history figure? ",
"A word that defines you: "]

response = []

print("Welcome to the Band Name Genrator.");

for quest in answers:
	item = input(quest + '\n')
	response.append(item)
	

for i in range(1 ,11):
	print(i , "Name: ", random.choice(response), random.choice(response))

 
