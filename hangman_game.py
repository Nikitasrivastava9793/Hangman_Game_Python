import random
stages=['''
  +---+
  |   |
  0   | 
 /|\  |
 / \  |
      | 
=========
        ''', '''  
   +---+
  |   |
  0   | 
 /|\  |
 /    |
      | 
=========
        ''', '''
  +---+
  |   |
  0   | 
 /|\  |
      |
      | 
=========
        ''', '''
  +---+
  |   |
  0   | 
 /|   |
      |
      | 
=========
        ''', '''
  +---+
  |   |
  0   | 
  |   |
      |
      | 
=========
        ''', '''
  +---+
  |   |
  0   | 
      |
      |
      | 
=========
        ''', '''
   +---+
  |   |
      |
      |
      |
      | 
=========
        ''' ]                                
list_of_fruits=["apple","grapes","orange"]
chosen_fruit=random.choice(list_of_fruits)
print(chosen_fruit)
lives=6
display=[]
for i in range(0,len(chosen_fruit)):
    display+="_"
print(display)
result=False
while not result:
    guess=input(f"ENTER THE LETTER YOU WANT TO CHECK\n")
    guess=guess.lower()
    for position in range(0,len(chosen_fruit)):
        letter=chosen_fruit[position]
        if letter==guess:
            display[position]=letter
    if guess not in chosen_fruit:
            lives=lives-1
            if lives==0:
             result=True
             print("you lose")
    print(f"{''.join(display)}")
    if "_" not in display:
           result=True 
           print("you win") 
    print(stages[lives])   
        