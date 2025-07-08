from fastapi import FastAPI
from langserve import add_routes # i want to convert everything to route, "routes" means anyone can hit and will get the particular result
from diagonistics_graph import build_graph

app = FastAPI()
graph = build_graph()



add_routes(app,graph,path="/diagnose")

# Inside "/diagnose" this partcular path, we will be able to access the graph, this is also customize name