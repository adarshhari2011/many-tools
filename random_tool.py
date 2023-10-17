import random
def username():
  words1=["Car","Fox","Cat"]
  words2=["Truck","Fish","Bird"]
  words3=["Van","Bannana","Light"]
  username=""
  for i in range(3):
    username += random.choice(words1+words2+words3)
  print(username)
def password(Alphabet_Type,Symbols_Numbers,Length):
  Alphabet_Lower = "abcdefghijklmnopqrstuvwxyz"
  Alphabet_Upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  Numbers = "0123456789"
  Symbols = "!@#$%^&*()-_+"
  Password = ""
  for x in range(Length):
      if Alphabet_Type == 1 and Symbols_Numbers == 1: 
          Password += random.choice(Alphabet_Lower+Symbols)
      elif Alphabet_Type == 1 and Symbols_Numbers == 2:
          Password += random.choice(Alphabet_Lower+Numbers)
      elif Alphabet_Type == 2 and Symbols_Numbers == 1:
          Password += random.choice(Alphabet_Lower+Numbers)
      elif Alphabet_Type == 1 and Symbols_Numbers == 3:
          Password += random.choice(Alphabet_Lower+Symbols+Numbers)     
      elif Alphabet_Type == 2 and Symbols_Numbers == 2:
        Password += random.choice(Alphabet_Upper+Symbols+Numbers)
      elif Alphabet_Type == 2 and Symbols_Numbers == 2:
        Password += random.choice(Alphabet_Upper+Numbers)
      elif Alphabet_Type == 3 and Symbols_Numbers == 3:
        Password += random.choice(Alphabet_Upper+Alphabet_Lower+Symbols+Numbers)
      elif Alphabet_Type == 3 and Symbols_Numbers == 1:
        Password += random.choice(Alphabet_Upper+Alphabet_Lower+Symbols)
      elif Alphabet_Type == 3 and Symbols_Numbers == 2:
        Password += random.choice(Alphabet_Upper+Alphabet_Lower+Numbers)



  return Password

def dice_throw():
  x=random.randint(1,6)
  return x
def toss():
  coin=["Heads","Tails"]
  return random.choice(coin)
def cards():
  cards=["Clubs","Diamonds", "Hearts", "Spades",]
  number=[1,2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]
  return  random.choice(cards),random.choice(number)
  