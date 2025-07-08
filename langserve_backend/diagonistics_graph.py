from typing import TypedDict
from langgraph.graph import StateGraph,END
from langchain_core.runnables import RunnableLambda
from tools.diagnosis_tool import ai_diagnos
from tools.symptom_checker import check_symptom


class DiagnosticState(TypedDict):
    input:str
    symptom_area : str
    diagnosis: str
    
def build_graph():
    graph = StateGraph(DiagnosticState)  
    # we are going to create symptom & diagnosis node , these nodes are technically call my tools basically
    # when ever we call symptom node, it call "check_symptom" tool, we call diagnosis node, it should call "ai_diagnos" tool
    
    def symptom_step(state):
        return {
                "input":state["input"],
                "symptom_area" : check_symptom.invoke(state["input"]), # whenever this node will be executed, it will call the "check_symptom" tool
                # whenever we invoke this one, it will try the to take the input, whatever input the user has given
                "diagnosis": state.get("diagnosis","")
        }
    
    graph.add_node("symptomcheck",RunnableLambda(symptom_step)) # make the "symptom_step" node as the node, 
    
    # "RunnableLambda(symptom_step)" means this node will be holding the particular function as "symptom_step"
    
    def diagnosis_step(state):
        return {
                "input":state["input"], # Taking input from the current state
                "symptom_area" : state['symptom_area'],
                "diagnosis":ai_diagnos.invoke(state['input']) # call "ai_diagnos" tool
        }
        
        
    graph.add_node("Aidiagnosis" , RunnableLambda(diagnosis_step))
    
    # After building two independent node, we will be going to connect these nodes
    graph.set_entry_point("symptomcheck")
    graph.add_edge("symptomcheck","Aidiagnosis") # we are creating edge between two nodes
    graph.add_edge("Aidiagnosis",END)
    
    return graph.compile()

