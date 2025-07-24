from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response, JSONResponse

app = FastAPI()

#Q1- Créer une route GET /hello, qui ne prend rien en paramètres
# et qui retourne le message “Hello world” dans le corps de la réponse
# avec un code de status 200 OK. (3 points)

@app.get("/hello")
def read_hello():
    return JSONResponse(
        content={"message": "Hello World"},
        status_code=200,
        media_type="application/json"
    )

#Q2- Créer une route GET /welcome, qui prend le paramètre de requête
# “name” de type chaîne de caractère, et qui retourne le message
# “Welcome <name>” comme corps de la réponse avec une code de status 200 OK,
# où <name> est la valeur du paramètre fourni. Le corps de la réponse peut être
# soit en texte brute, soit en JSON avec l’attribut de votre choix, mais pas
# les deux. (3 points)

@app.get("/welcome")
def read_welcome(name: str):
    return JSONResponse(
        content={"message": f"Welcome {name}"},
        status_code=200,
        media_type="application/json"
    )

#Q3- Créer une route POST /students, qui prend dans le corps de la requête
# une liste d’objet JSON qui a les attributs suivants :
    #- Reference, de type chaîne de caractères
    #- FirstName, de type chaîne de caractères
    #- LastName, de type chaîne de caractères
    #- Age, de type nombre entier
# Le comportement attendu par cette requête est de mémoriser en mémoire (vive),
# la liste des objets qui ont été fournis à travers le corps de la requête, et
# la réponse attendue est de retourner la liste contenant les objets students
# mémorisés en mémoire vive, c’est à dire ceux qui viennent d’être ajoutés et
# ceux qui ont déjà existés avant l’ajout. Le code de statut attendu possède
# la signification CREATED et pas le code de statut générique dont la
# signification est OK (3 points)

@app.post("/students")
def read_student():
    return

#Q4- Créer une route GET /students qui ne prend rien en paramètre, et qui
# retourne le contenu de la liste d’objets students actuellement stockés en
# mémoire avec un code de status 200 OK.. (2 points)


#Q5- Créer une requête idempotente à travers une nouvelle route PUT /students,
# en utilisant l’attribut “Reference” comme identifiant unique. Autrement dit,
# si la Reference fournie dans le corps existe déjà, alors effectuer une
# modification si les valeurs ont été modifiées, sinon effectuer un ajout.
# (4 points)


#Q6-  Pour chaque route qui a été définie plus tôt, vous allez maintenant
# uploader un capture d’écran pour illustrer que vous maîtrisez Postman comme
# client HTTP. Pour cela :
#     - Créez un nouveau dossier intitulé “postman” dans votre projet
#     - Renommer chaque fichier de la capture respectivement selon la route que vous avez
#     créé précédemment. Par exemple, si votre route affichée sur Postman est GET /hello,
#     cela correspond à la Q1, donc vous allez renommer le fichier Q1.
#     Pour les 5 questions, vous devez donc avoir 5 images de captures d’écran intitulées
#     Q1 jusqu’à Q5, si vous avez tout terminé.