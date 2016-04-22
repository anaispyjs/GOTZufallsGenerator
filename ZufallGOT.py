import random
characters = ['Cersei','Jon Schnee','Jaime', 'Arya','Sansa','Kleinfinger','Daenerys','Tyrion','Margaery']
textbausteine = [ 'ist ein Kind von','stirbt.','kriegt bald ein Kind.', 'ist in Wahrheit ein Tagaryen.']

chara = random.randint(0,9)
charakter = characters[chara]
charazwei = random.randint(0,9)
charakterzwei = characters[charazwei]
text = random.randint(0,3)
textbaustein = textbausteine[text]
if text == 0:
    print(charakter + ' ' + textbaustein + ' '+ charakterzwei)
else:
    print(charakter + ' ' + textbaustein)
    
    
