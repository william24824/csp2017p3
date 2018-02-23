# Spiderman's Crazy Story
# Action Fiction
# William Flores
print "Spiderman's first Threat"
print ("\n")
def introduction():
  print "Peter Parker is 16 years old and lives in New York City. He's only been Spiderman for a couple months now. It has been really hard for Peter being Spiderman and being a kid sometimes. Keeping his secret from his aunt and everyone else even close friends. He's had some experience now with his super abilities. Peter has created his webshooters and created web-fluid in chemistry"
  print ("\n")
  print "Peter goes to Washington for The Academic Decathlon Event they stay in a hotel nearby.  Peter sneaks out the hotel room at night, but all the teenagers sneak out at night to go swimming but he has to go fight a villian in Maryland."
  print ("\n")
  swim_fight()
  
def swim_fight():
  print "Should Peter go to swimming with his friends and his crush Liz or go fight the Chameleon in his base?"
  print ("\n")
  print "Type s for swimming or f for fighting the Chameleon."
  answer = raw_input()
  if answer == "s":
      print "swimming"
      Liz_Ned()
  else:
    print "chameleon"
    climb_inside()
    
def Liz_Ned():
  print ("\n")
  print "Peter swims with the team.  Should he go talk to his crush Liz or talk to his bestfriend Ned?"
  print "Type l for Liz or n for Ned."
  answer = raw_input()
  if answer == "n":
    print "Ned"
    Ned()
  else:
    print "Liz"
    Liz()

def Ned():
  print ("\n")
  print "Ned thanks you for not leaving him, but Liz feels lonely and really wanted Peter to hangout with her in the pool."
  print ("\n")
  print "Liz hangs out with her other friend and Peter later asks her to go to the dance with him. She says yes and they go together. Thank you for playing the story of Peter/Spider-Man!"
  print ("\n")

def Liz():
  print ("\n")
  print "Peter hangs out with Liz although Peter is very happy and finally talking to Liz Ned feels lonely.  Ned is a bit mad at Peter for choosing Liz over Ned.  Ned forgives Peter and they all go to the homecoming dance with Liz and the other teammates from the Academic Decathlon team."
  print ("\n")
  print "Thanks for playing the story of Peter/Spider-Man!"
  
def climb_inside():
  print ("\n")
  print "Peter decides to go and stop the Chameleon .  While Peter fights the Chameleon he fails to capture him and gets knocked out when he accidentally knocked himself out.  Peter finds himself in a facility and can't get out.  He realizes it's the day of the Academic Decathlon event but he's stuck in a facility.  He he has new upgrades in his suit because Ned unlocked them he has a AI in his suit who he names Karen. Karen helps Peter get out the facility as he soon realizes he basically gave a bomb to Ned. "
  print ("\n")
  print "Peter runs to the Washington Monument should he climb it and stop the elevator from falling or run inside and stop it from there?"
  print ("\n")
  print "Type c for climb or i for inside."
  answer = raw_input()
  if answer == "c":
    print "climb"
    climb()
  else:
    print "inside"
    inside()
    
def climb():
  print ("\n")
  print "Peter climbed the wall and jumped from the top of the Washington Monument glided over the helicopter and broke through the window and shot a web at the elevator and caught it, he pulled it up and all the kids got out safe! Thanks for listening to the story of Peter/Spider-Man!"

def inside():
  print ("\n")
  print "Peter runs inside and shoots his webs to slow down and stop the elevator from crashing down into the ground and the kids are all safe."
  print ("\n")
  print "After all of that they all go home and Peter will soon get his payback and defeat the Chameleon this is the story of Peter/Spider-Man."
  
introduction()