from hero import Warrior, Assasin, Support
warrior = Warrior("bambang", pos_x=10)
assasin = Assasin("joko", pos_x=25)
support = Support("udin",pos_x=30)
# sebelum
print("health (before)", warrior.getHealth())
assasin.attack(warrior)
# sesudah
print("health (after)", warrior.getHealth())
print("-"*10)
# sebelum
print("Warrior (health)", warrior.getHealth())
print("Support (speed) : ",support.getSpeed())
support.special(warrior)
# sesudah
print("Warrior (health)", warrior.getHealth())
print("Support (speed): ",support.getSpeed())

# SPECIAL
print('===SPECIAL===')

# sebelum
print('warrior>assasin')
print("Warrior (power)", warrior.getPower())
print("Warrior (armor) : ", warrior.getArmor())
print(assasin.getHealth())
warrior.special(assasin)
# sesudah
print("Warrior (power)", warrior.getPower())
print("Warrior (armor) : ", warrior.getArmor())
print(assasin.getHealth())

print('=====================')

# sebelum
print('assasin>support')
print("Assasin (power)", assasin.getPower())
print("Assasin (armor) : ", assasin.getArmor())
print(support.getHealth())
assasin.special(support)
# sesudah
print("Assasin (power)", assasin.getPower())
print("Assasin (armor) : ", assasin.getArmor())
print(support.getHealth())

print('=======================')

#sebelum
print('support>warrior')
print("Warrior (health)", warrior.getHealth())
print("Support (speed) : ", support.getSpeed())

support.special(warrior)

#sesudah
print("Warrior (health)", warrior.getHealth())
print("Support (speed : ", support.getSpeed())
