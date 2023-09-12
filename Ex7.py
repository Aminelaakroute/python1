T = float(input("Veuillez entre la temperature :"))
if T < 0 :
    print("L'état de leau est Glase")
elif T > 100 :
    print("L'état de leau est Vapeur")
else :
    print("L'état de leau est Liquide")