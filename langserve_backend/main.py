from fastapi import FastAPI
from langserve import add_routes # i want to convert everything to route, "routes" means anyone can hit and will get the particular result
from diagonistics_graph import build_graph

app = FastAPI()
graph = build_graph()

# langserve_backend/auth.py    This below portion is for the authentication purpose 
from fastapi import Header, HTTPException, Security # 
from fastapi.security.api_key import APIKeyHeader

API_KEY_NAME = "Authorization"
API_KEY = "secret-token-123"  # change this to a strong key or read from ENV

# we can also make this "API_KEY" dynamic for everyone, we can write another function to generate the key that way i want

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)
# create the simple function, this simple function is trying to use the "Security", which is the feature of the fastAPI. 
# It will ask for the "API_KEY_NAME" & "API_KEY", as we are providing for the EURI_API_KEY
def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key != f"Bearer {API_KEY}":
        raise HTTPException(status_code=403, detail="Unauthorized access")
    return api_key


add_routes(app,graph,path="/diagnose",dependencies = [Depends(verify_api_key)]) # The way as we are depending on the EURI_API_KEY,
# It will take the API_KEY and give the final authentication



# Inside "/diagnose" this partcular path, we will be able to access the graph, this is also customize name