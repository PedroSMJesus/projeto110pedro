import random

def game(response):
  while response == "y":
    
    no = random.randint(1,6)
    
    if(no == 1):
        print("[ - - - ]")
        print("[       ]")
        print("[   0   ]")
        print("[       ]")
        print("[ - - - ]")
        response = input("dijite y para jogar o dado: ")

    if(no == 2):
        print("[ - - - ]")
        print("[ 0     ]")
        print("[       ]")
        print("[     0 ]")
        print("[ - - - ]")
        response = input("dijite y para jogar o dado: ")    

    if(no == 3):
        print("[ - - - ]")
        print("[       ]")
        print("[ 0 0 0 ]")
        print("[       ]")
        print("[ - - - ]")
        response = input("dijite y para jogar o dado: ")    

    if(no == 4):
        print("[ - - - ]")
        print("[ 0   0 ]")
        print("[       ]")
        print("[ 0   0 ]")
        print("[ - - - ]")
        response = input("dijite y para jogar o dado: ")    
    
    if(no == 5):
        print("[ - - - ]")
        print("[ 0   0 ]")
        print("[   0   ]")
        print("[ 0   0 ]")
        print("[ - - - ]")
        response = input("dijite y para jogar o dado: ") 

    if(no == 6):
        print("[ - - - ]")
        print("[ 0 0 0 ]")
        print("[       ]")
        print("[ 0 0 0 ]")
        print("[ - - - ]")  
        response = input("dijite y para jogar o dado: ")   

response = input("dijite y para jogar o dado: ")

game(response)