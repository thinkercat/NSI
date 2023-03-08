import json


with open("/home/nsi/Documents/NSI/html/JDR-templates/pythonBasics/history.json", "r") as hd:
    value = json.load(hd)

class Node():
    def __init__(self, history_data, json_node_id) -> None:
        '''
        ::params::
        json_data_node Représent l'id du noeud que vous souhaitez ex: 01f0 
        '''
        value = history_data
        id = json_node_id
        luck = value[json_node_id]["luck"]
        require = value[json_node_id]["require"]
        cost = value[json_node_id]["cost"]
        content = value[json_node_id]["content"]
    
class History():
    def __init__(self, name:str = "defaultName", description:str = "defaultDescription", author:str = "defultAuthor", history_json_file_path:str = "/home/nsi/Documents/NSI/html/JDR-templates/pythonBasics/history.json") -> None:
        '''
        ::params::
        '''
        self.name = name
        self.description = description
        self.author = author
        with open(history_json_file_path, 'r') as hd:
            self.history_data = json.load(hd)
        self.nodes = {}
    
    def loadNodes(self):

        for e in self.history_data:
            print(e)
            self.nodes[e] = Node(self.history_data, e)
            print(self.nodes)

histoire = History()
histoire.loadNodes()


    
