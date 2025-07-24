from fastapi import FastAPI
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import Response, JSONResponse

app = FastAPI()

#Q1-Créer une route GET /hello, qui ne prend rien en paramètres
# et qui retourne le message “Hello world” dans le corps de la réponse
# avec un code de status 200 OK. (3 points)
@app.get("/hello")
def read_hello():
    return JSONResponse(
        content={"message": "Hello World"},
        status_code=200,
        media_type="application/json"
    )

#Q2-Créer une route GET /welcome, qui prend le paramètre de requête
# “name” de type chaîne de caractère, et qui retourne le message
# “Welcome <name>” comme corps de la réponse avec un code de status 200 OK,
# où <name> est la valeur du paramètre fourni. Le corps de la réponse peut être
# soit en texte brut, soit en JSON avec l’attribut de votre choix, mais pas
# les deux. (3 points)
@app.get("/welcome")
def read_welcome(name: str):
    return JSONResponse(
        content={"message": f"Welcome {name}"},
        status_code=200,
        media_type="application/json"
    )

#Q3-Créer une route POST /students, qui prend dans le corps de la requête
# une liste d’objet JSON qui a les attributs suivants :
    #- Reference, de type chaîne de caractères
    #- FirstName, de type chaîne de caractères
    #- LastName, de type chaîne de caractères
    #- Age, de type nombre entier
# Le comportement attendu par cette requête est de mémoriser en mémoire (vive),
# la liste des objets qui ont été fournis à travers le corps de la requête, et
# la réponse attendue est de retourner la liste contenant les objets students
# mémorisés en mémoire vive, c'est-à-dire ceux qui viennent d’être ajoutés et
# ceux qui ont déjà existés avant l’ajout. Le code de statut attendu va posséder
# la signification CREATED et pas le code de statut générique dont la
# signification est OK (3 points).

class StudentRequest(BaseModel):
    reference: str
    first_name: str
    last_name: str
    age: int
@app.post("/students")
def create_student(request: StudentRequest):
    return JSONResponse(
        content={"student": f"{request.reference}: {request.first_name} {request.last_name}, {request.age}"},
        status_code=201,
        media_type="application/json"
    )

#Q4-Créer une route GET /students qui ne prend rien en paramètre, et qui
# retourne le contenu de la liste d’objets students actuellement stockés en
# mémoire avec un code de status 200 OK. (2 points)
@app.get("/students")
def read_student():
    return JSONResponse(
        content={},
        status_code=200
    )

#Q5-Créer une requête idempotente à travers une nouvelle route PUT /students,
# en utilisant l’attribut “Reference” comme identifiant unique. Autrement dit,
# si la Reference fournie dans le corps existe déjà, alors effectuer une
# modification si les valeurs ont été modifiées, sinon effectuer un ajout.
# (4 points)
@app.put("/students")
def put_student():
    return

@app.get("/students-authorized")
def read_rood(request: Request):
    headers = request.headers
    if "Authorization" in headers:
        return JSONResponse(
            content={"status": "FORBBIDEN", "message": "Authorization denied"},
            status_code=403,
            media_type="application/json"
        )
    authorization = headers.get("Authorization")
    if authorization != "bon courage":
        return JSONResponse(
            content={"status": "FORBBIDEN", "message": "Unknown authorization"},
            status_code=403,
            media_type="application/json"
        )
    return {"..."}
