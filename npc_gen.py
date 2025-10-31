import random
start=""
while start != "yes":
    start=input("ready to start the generator? Type yes to start.")

malenames=["Geraldine","Peter","Derrick","Eugene","Joseph"]
femalenames=["Hailey","Madison","Irene","Cassidy","Lexi"]
male=(random.choice(malenames))
female=(random.choice(femalenames))
genderlist=[male,female]
gender=random.choice(genderlist)
if gender==male:
  charnames=(male)
elif gender==female:
  charnames=(female)
atcharnames=charnames
Heights=["1.1","1,2","1.3","1.4","1.5","1.7","1.8","2.0","2.5"]
atheight=(random.choice(Heights))
strength=[10,20,30,40,50,60,70,80,90,100]
atstrength=(random.choice(strength))
agility=["very low","low","medium","high-medium","high", "very high"]
atagility=(random.choice(agility))
print(atagility)





  






     
 