import json

class Node():
    def __init__(self, history_data, json_node_id, ) -> None:
        '''
        :params:
        json_node_id Représente l'id du noeud que vous souhaitez ex: 01f0 
        '''
        self.value = history_data
        self.id = json_node_id
        self.luck = self.value[json_node_id]["luck"]
        self.require = self.value[json_node_id]["require"]
        self.cost = self.value[json_node_id]["cost"]
        self.content = self.value[json_node_id]["content"]
    
class History():
    def __init__(self, name:str = "defaultName", description:str = "defaultDescription", author:str = "defultAuthor", history_json_file_path:str = "NSI/html/JDR-templates/pythonBasics/history.json") -> None:
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
        '''
        Create Node Object for nodes in json data
        '''
        for e in self.history_data:
            self.nodes[e] = Node(self.history_data, e)



histoire = History()
histoire.loadNodes()




    
