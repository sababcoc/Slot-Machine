import random
def compare(reel1,reel2,reel3):
  if reel1==reel2 or reel2==reel3 or reel3==reel1:
    return ("win1")
  elif reel1==reel2 and reel1==reel3:
    return("win2")
  else:
    return("y")



def reel():
  reel=random.randint(0,9)
  return (reel)
 
    
# Your main() method accepts one argument.  The value of the argument is stored in a variable called "balance" (See line 9)
def main(balance):
  print("$"+str(balance))
  bet=(input("how much would you like to bet? $"))
  bet=float(bet)
  balance=float(balance)
  bet=round(bet,2)
  balance=round(balance,2)
  balance=balance-bet
  print("$"+str(bet))
  print("$"+str(balance))
  reel1=reel()
  reel2=reel()
  reel3=reel()
  win1=bet*1
  win2=bet*1.5
  x=compare(reel1,reel2,reel3)
    
  if x=="win1":
    newbalance=(balance+win1)
  elif x=="win2":
    newbalance=(balance+win2)
  else:
    newbalance=balance
    
  newbalance=round(newbalance,2)

  print(">>"+str(reel1)+"<< >>"+str(reel2)+"<< >>"+str(reel3)+"<<")
  
  if x=="win1"or x=="win2":
    print("you win:$ "+str(newbalance))
  else:
    print ("$"+str(newbalance))
  balance=newbalance
  if balance > 0:
    main(balance)
    
  
  

# Start your program with the main() method
# Set the initial balance for the user to 10000
if __name__=="__main__":
  main(10000)