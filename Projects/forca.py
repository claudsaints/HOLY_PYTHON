import random

# list pf words

words = ['maça','chocolate','arroz']

# the chosen word

word = random.choice(words)
word_length = len(word)

# display at _ in positions

display = []

for _ in range(word_length):
    display += "_"
print(display)
# player input 

end = False
life = 6

# loops 

while not end and life != 0:
    player_letter = input('Choice your letter').lower()
    for position in range(word_length):
        letter = word[position]    
        if letter == player_letter:
            display[position] = letter


    if player_letter not in word:
        life-= 1       
    print(display)
    print(life)
    if "_" not in display:
        end=True
        print("You Win")
    elif life == 0:
        print('You Lose')

