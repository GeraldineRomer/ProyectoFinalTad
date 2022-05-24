from circle import circle
from line import line
class treeNodes:
    class Node:
        def __init__(self,value,x,y):
            self.value = value
            self.left_node = None
            self.right_node = None
            self.circle = None
            self.line_right = None
            self.line_left = None
            self.x = x
            self.y = y
            
    def __init__(self,display):
        self.root = None
        self.lenght_nodes = 0 
        self.display = display
        self.circle_color = (149, 243, 108)
        #self.line_color = (149, 243, 108)
        
    def add(self, value, x, y):
        new_node = self.Node(value,x,y)
        new_node.circle = circle(self.display,self.circle_color,value,x,y).crear()
        if self.root == None:
            self.root = new_node
        else:
            def recorrer (value, node):
                if value == node.value:
                    return "El elemento ya existe"
                elif value < node.value:
                    if node.left_node == None:
                        node.left_node = new_node
                        node.line_left = line(self.display,self.circle_color,node.x,node.y,node.left_node.x,node.left_node.y).crear()
                        
                        return True
                    else:
                        return recorrer(value, node.left_node)
                elif value > node.value:
                    if node.right_node == None:
                        node.right_node = new_node
                        node.line_right = line(self.display,self.circle_color,node.x,node.y,node.right_node.x,node.right_node.y).crear()
                        
                        return True
                    else:
                        return recorrer(value, node.right_node)
        
            recorrer(value, self.root)
        
                    
    def find (self, value,color):
        def recorrer(value, node):
            if value == node.value:
                node.circle = circle(self.display,color,value,node.x,node.y).crear()
                return node.value
            elif value < node.value:
                if node.left_node == None:
                    return "No existe el elemento buscado"
                else:
                    node.line_left = line(self.display,color,node.x,node.y,node.left_node.x,node.left_node.y).crear()
                    return recorrer(value, node.left_node)
            else:
                if node.right_node == None:
                    return "No existe el elemento buscado"
                else:
                    node.line_right = line(self.display,color,node.x,node.y,node.right_node.x,node.right_node.y).crear()
                    return recorrer(value, node.right_node)
        nodo_encontrado = recorrer(value, self.root)
        #return print(nodo_encontrado)
        
    def preorder (self):
        #RID(Raíz, izquierda, derecha)
        container = []
        def recorrer(node):
            container.append(node.value)
            if node.left_node != None:
                recorrer(node.left_node)
            if node.right_node != None:
                recorrer(node.right_node)
        recorrer(self.root)
        print(f"Preorder -> {container}")
        return container
    
    def inorder(self):
        #IRD (Izquierda, raíz, derecha)
        container = []
        def recorrer(node):
            if node.left_node != None:
                recorrer(node.left_node)
            container.append(node.value)
            if node.right_node != None:
                recorrer(node.right_node)
        recorrer(self.root)
        print(f"Inorder -> {container}")
        return container
    
    def postorder(self):
        #IDR(Izquierda, derecha, raíz)
        container = []
        def recorrer (node):
            if node.left_node != None:
                recorrer(node.left_node)
            if node.right_node != None:
                recorrer(node.right_node)
            container.append(node.value)
        recorrer(self.root)
        print(f"Postorder -> {container}")
        return container
            
    def breadth_first_search(self):
        #si el contenedor 1 tiene como longitud 1 quiere decir que el arbol al menos tiene un nodo que es la raíz
        container_1 = [self.root]
        container_2 = [self.root.value]
        while len(container_1) != 0:
            node = container_1[0]
            if node.left_node != None:
                container_1.append(node.left_node)
                container_2.append(node.left_node.value)
            if node.right_node != None:
                container_1.append(node.right_node)
                container_2.append(node.right_node.value)
            container_1.pop(0)
        print(f"Amplitud -> {container_2}")
        return container_2
    
    def actulizar_color_linea (self, value):
        def recorrer(value, node):
            if value == node.value:
                node.circle = circle(self.display,self.circle_color,value,node.x,node.y).crear()
                return node.value
            elif value < node.value:
                if node.left_node == None:
                    return "No existe el elemento buscado"
                else:
                    node.line_left = line(self.display,self.line_color,node.x,node.y,node.left_node.x,node.left_node.y).crear()
                    return recorrer(value, node.left_node)
            else:
                if node.right_node == None:
                    return "No existe el elemento buscado"
                else:
                    node.line_right = line(self.display,self.line_color,node.x,node.y,node.right_node.x,node.right_node.y).crear()
                    return recorrer(value, node.right_node)
        nodo_encontrado = recorrer(value, self.root)
   