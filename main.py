import random
NB_MIN=1
NB_MAX=10
NB_QUESTION = 4


def pose_question():
    a= random.randint(NB_MIN,NB_MAX)
    b= random.randint(NB_MIN,NB_MAX)
    resultat= int(a+b)
    reponse_str = input (f" Calculez : {a} + {b}  = ")
    reponse_int= int(reponse_str)
    if resultat== reponse_int : 
        print(" Réponse Correct")
    else : 
        print("Réponse incorrect")
    

for  i in range(0,NB_QUESTION):
    print(f"Question n° {i} sur {NB_QUESTION} ")
    pose_question()
    print()