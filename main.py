import preciousGems

def main():
    num_gems = int(input("How many types of gems are you interested in?:"))

    while num_gems < 1:
      num_gems = int(input("Amount must be >= 1: "))
    
    for i in range(num_gems):
      name = input("\nEnter the name of gem: ")
      carats = float(input("Enter the number of carats (> 0) : "))
      while carats < 0:
        carats = float(input("Number of carats must be > 0: "))
      

      gem = preciousGems.PreciousGems(name, carats)
      
      print(gem)
      


main()
