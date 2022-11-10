# control flow exercise from Codecademy, including If, elif, else statements, boolean and logical operators
# this exercise is all a magic 8 ball program that gives you random answers based on chance
# requires to create 10 different responses based on number 1-10
# In this context, it was created to see the chances of getting a random video game character

import random
name = "Xiao"
question = "Will I get Itto?"

answer ="" # where the final answer will be stored after the number chosen

random_number= random.randint(1, 10)
#print(random_number)
if random_number==1:
  answer = "Yes- definitely"
elif random_number==2:
  answer="It is decidedly so"
elif random_number==3:
  answer="Without a doubt."
elif random_number==4:
  answer="Reply hazy, try again."
elif random_number==5:
  answer="Ask again later."
elif random_number==6:
  answer="Better not tell you now."
elif random_number==7:
  answer="My sources say no."
elif random_number==8:
  answer="Outlook not so good."
elif random_number==9:
  answer="Very doubtful."
elif random_number==10:
  answer="5 Star!"
else:
  answer="Error"

print("Question: " + question)

print("Mihoyo's answer: "+ answer)
