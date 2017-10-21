import random
import turtle
import time

print("You are a pokemon trainer with a pikachu, charmander, squirtle and bulbasaur wandering around on a beautiful island.")
time.sleep(2)
print("But this dream soon turns into a nightmare.")
time.sleep(2)
print("You are now stuck in the midst of nowhere.")
time.sleep(2)
print("And soon you and your pokemons are going to get very hungry and tired")
time.sleep(2)
print("There is plenty of wild food here to eat but BEWARE...")
time.sleep(2)
print("There are wild pokemons too..")
time.sleep(2)
print("Defeat these pokemons to get enough HP")
time.sleep(2)
print("Your charmander can evolve into a charizard and we can all get out.")
time.sleep(2)

input_user = input("\nAre you ready for the battle? Y/N")
if input_user == "Y":
  print "good choice! Go on, if the time comes, I'll watch over you."
elif input_user == "N":
  print "But your pokemons are tired and hungry and you are stuck on this island"
  time.sleep(2)
  print "wild pokemons come and attack your charmander anyway... Better luck next time!"
  exit()
else:
  print "Wrong choice."
  

screen = turtle.Screen()
screen.setup(500, 600)
screen.addshape("ash_pokemon.jpg")
turtle.left(90)
turtle.shape("ash_pokemon.jpg")

def find_hp(pokemon_choice):
  if pokemon_choice == "charmander":
    screen.addshape("charmander.jpg")
    turtle.shape("charmander.jpg")
    hp = 39
    attack = 52
    defence = 43
  elif pokemon_choice == "bulbasaur":
    screen.addshape("bulbasaur.jpg")
    turtle.shape("bulbasaur.jpg")
    hp = 45
    attack = 49
    defence = 49
  elif pokemon_choice == "squirtle":
    screen.addshape("squirtle.jpg")
    turtle.shape("squirtle.jpg")
    hp = 44
    attack = 48
    defence = 65
  elif pokemon_choice == "pikachu":
    screen.addshape("pikachu.jpg")
    turtle.shape("pikachu.jpg")
    hp = 35
    attack = 55
    defence = 40
  else:
    print "You dont have this pokemon"
    find_hp(pokemon_choice)
  return hp
  
def attack(myPokemon, computerPokemon, hp, hpC): #can add attack and defence
  if hp > hpC:
    hp = hp + 10
    print("Great job! You won this battle..")
  else:
    hp = hp - 5
    print("Alas! You lost this one. But, don't worry you have more to come.")
  if hp > 77:
    print("Wait up! Stand back... your charmander is evolving...")
    screen.addshape("charizard.jpg")
    turtle.shape("charizard.jpg")
  return hp


myPokemons = ["charmander", "bulbasaur", "squirtle", "pikachu"]
computerPokemons = ["onyx", "squirtle", "warturtle", "weedle", "pidgeotto", "ekans"]

myChoice = random.choice(myPokemons)
hp = find_hp(myChoice)

while hp < 78 or hp > 0:
  time.sleep(3)
  hpC = random.randint(34,46)
  computerChoice = random.choice(computerPokemons)
  print "\n\nYou have come across a wild %s" % computerChoice
  print "\nDo you want to battle it now or Analyse the situation first"
  battle_choice = input("Do you want to battle it now? Y/N")
  if battle_choice == "Y":
    hp = attack(myChoice, computerChoice, hp, hpC)
  else:
    print "HP of %s is %d" %(myChoice,hp)
    print "HP of %s is %d" %(computerChoice,hpC)
    time.sleep(1)
    battle_choice = input("\nDo you want to battle it now? Y/N")
    if battle_choice == "Y":
      hp = attack(myChoice, computerChoice, hp, hpC)
    elif battle_choice == "N":
      print " Go on, maybe another pokemon will help you get out!"
      
if hp < 0 or hp == 0:
  print("Your %s lost all their energy.") % myChoice
  print("Unfortunately for you, the game ends here.")
