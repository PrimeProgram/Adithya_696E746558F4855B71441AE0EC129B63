#Define the parent class
class Player:
  def play(self):
    print("The player is playing cricket.")

#First Derived class Batsman
class Batsman(Player):
  def play(self):
    print("The batsman is batting")

#Second Derivced class Bowler
class Bowler(Player):
  def play(self):
    print("The bowler is bowling")

#Creating objects for both classes
batsman = Batsman()
bowler = Bowler()

batsman.play()
bowler.play()

#Implementing hierarchical inheritance