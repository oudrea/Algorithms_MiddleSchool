if __name__ == '__main__':
  min=0
  max=int(input("Enter your maximum:"))
  guesses = 0
  while True:
    print(f"Our guess is {(min+max)//2}")
    guesses = guesses + 1
    z = input("How did we do? (enter h, l or e):")
    if z=="e":
        print("Yay!")
        break
    else:
        if z=="l" :
            max=(min+max)//2-1
        elif z=="h": 
            min=(min+max)//2+1
        else:
            print("Stop fooling around or I will find you!!!!!!")

  print(f"I used {guesses} guesses")