import random
name=["devid","ace","mark","rogan","thomas"]
fav_food=["pizza","burger","bibimbab","menemen"]
city=["NYC","LA","TOKYO","ISTANBUL","HONOLULU","SF"]
work=["actor","singer","engineer","doctor","advocate"]
car=["bmw","thar","lamborghini","bugatii","mclaren"]
married=["married","unmarried"]

print('my name is '+random.choice(name)+
      '.\n'+'  i like to eat  '+random.choice(fav_food)+'.\n'+' i live in  '
      +random.choice(city)+'.\n'+' i am a '+random.choice(work)+
      '.\n'+ '  i have a '+ random.choice(car)+
      '.\n'+' i am '+random.choice(married)+'.')
