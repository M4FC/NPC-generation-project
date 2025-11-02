import random
import time
start=""
while start != "yes":
    start=input("ready to start the generator? Type yes to start.")
#the section above makes a user input section where the generator will only start when the user types yes
atstrength=random.randint(1,100)
atage=random.randint(1,95)
# lines 18-19 make strength and age attributes randomized with random.randint
names=["Geraldine","Peter","Derrick","Eugene","Joseph","Hailey","Madison","Irene","Cassidy","Lexi"]
atnames=random.choice(names)
Heights=["1.1","1,2","1.3","1.4","1.5","1.7","1.8","2.0","2.5"]
atheight=(random.choice(Heights))
agility=["very low","low","medium","high-medium","high", "very high"]
atagility=(random.choice(agility))
magic=["yes","no","no"] #extra no makes it so it more likely that npc's dont have magic
atmagic=random.choice(magic)
inteligence=["very low","low","medium","high-medium","high", "very high"]
atinteligence=random.choice(inteligence)
region=["South Nonvak","North Nonvak", "East Nonvak","West Nonvak","Vangel Island","Unknown"]
atregion=random.choice(region)
status=["lower class","lower class","lower class","lower class","middle class","middle class","noble class"]
#additional lower class and middle class make them more likely while noble class is rarer
atstatus=random.choice(status)
awareness=["very low","low","medium","high-medium","high", "very high"]
atawareness=random.choice(awareness)
atspeed=random.randint(1,100)
#code above makes attributes with a list and random.choice
npc_amount=int(input("how many npc's do you wish to generate"))
threshold=npc_amount*2
while npc_amount< threshold:
   npc_amount+=1
   print(f"Name:{random.choice(names)}\nAge:{random.randint(1,95)}\nStrength:{random.randint(1,100)}\nAgility:{random.choice(agility)}\nRegion:{random.choice(region)}\nHeight:{random.choice(Heights)}\nMagic:{random.choice(magic)}\nAwareness:{random.choice(awareness)}\nInteligence:{random.choice(inteligence)}\nStatus:{random.choice(status)}\nspeed:{random.randint(1,100)}\n")
   time.sleep(0.7)








  






     
 