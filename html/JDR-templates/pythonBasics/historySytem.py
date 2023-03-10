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
            self.nodes = json.load(hd)

        self.currentNode = 0



    def nextNode(self, nodeId):
        '''
        renvoie les prochains noeuds en fonctions du noeud mit en paramètre
        '''
        nextNodes = []
        pos = len(nodeId)

        for id in self.nodes:
            if len(id) == pos+1 and nodeId == id[0:pos]:
                nextNodes.append(id)

        return nextNodes

    def previousNode(self, nodeId):
        '''
        renvoie le noeud précèdent du noeud mit en paramètre
        '''
        for id in self.nodes:
            if nodeId[0:-1] == id:
                return id

    def run(self):
        currentNode = '0'

        while len(self.nextNode(currentNode)) > 0:
            print(self.nodes[currentNode]['content'])
            for nId in self.nextNode(currentNode):
                print(f"{nId} : {self.nodes[nId]['content']}")

            currentNode = str(input())
        

histoire = History()
histoire.run()




    
