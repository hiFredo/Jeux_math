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
        return True
    return False
    
nb_point= 0
for  i in range(0,NB_QUESTION):
    print(f"Question n° {i+1} sur {NB_QUESTION} :")
    reponse = pose_question()
    if reponse==True:
        print(" Réponse Correct")
        nb_point +=1
    else: 
        print("Réponse incorrect")
    print()
print(f"Votre score est {nb_point} sur {NB_QUESTION} ")
