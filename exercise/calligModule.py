import modHero

querySkill = input("select weapon:")

i = 0

for each_item in modHero.skill:
    if (each_item == querySkill):
        modHero.printItem(querySkill, i)
    i = i + 1

print ("---------------------------------")
print ("\n")
