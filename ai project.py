count=0
COUNT=0
print("Welcome to my quiz!")

playing = input("Do you want to play? ")

if playing.lower() ==  "yes": 
  print ("okay! let's play. Answer the following in yes/no ")
else:
  print("Okay! bye bye")
  exit()

answer=input( "Have you felt sad or upset lately?" )
if answer == "yes" :
  count+=1
else:
  COUNT+=1
answer= input("Do you feel lonely ?")
if answer == "yes" :
  count+=1
else:
  COUNT+=1
answer= input("Recently have you had trouble falling sleep?")
if answer == "yes" :
  count+=1
else:
  COUNT+=1
answer= input("Have you had episodes of poor appetite?")
if answer == "yes" :
  count+=1
else:
  COUNT+=1
answer= input("Have you ever felt bad about yourself?")
if answer == "yes" :
  count+=1 
else:
  COUNT+=1
answer= input("Have you felt that you have very little energy? ")
if answer == "yes" :
    count+=1
else:
    COUNT+=1
answer= input("Have you had difficulty in making decisions yourself lately?")
if answer =="yes":
      count+=1
else:
   COUNT+=1
answer= input("Have you had death or suicide thoughts lately?")
if answer == "yes":
        count+=1
else:
        COUNT+=1
answer= input("Have you been very restless recently?")
if answer == "yes":
          count+=1
else:
          COUNT+=1
answer= input("Do you see yourself as equally worthwhile&deserving as people whom you daily interact with?")
if answer == "yes":
           count+=1
else:
            COUNT+=1
if count >=5:
    print("You will be ok . Consult a Psychiatrist")
else:
    print("Not depressed ")