from queue import Queue

class BinaryTree:

    class __nodeTree:

        def __init__(self, value, other_values = None):
            self.value = value
            self.other_values = other_values
            self.left = None
            self.right = None
            self.height = 0

        def __str__(self):
            return str(self.value)+" "+str(self.other_values)

    def __init__(self):
        self.root = None

    def insert(self, value, other_values = None):
        def __insert(root, value, other_values):
            if root is None:
                return BinaryTree.__nodeTree(value, other_values)
            elif value < root.value:
                root.left = __insert(root.left, value, other_values)
            else:
                root.right = __insert(root.right, value, other_values)

            root = self.auto_balance(root)
            self.update_height(root)

            return root

        self.root = __insert(self.root, value, other_values)

    def pre_order(self):
        def __pre_order(root):
            if root is not None:
                print(root.value, root.other_values, root.height)
                __pre_order(root.left)
                __pre_order(root.right)

        if self.root is not None:
            __pre_order(self.root)

    def in_order(self):
        def __in_order(root):
            if root is not None:
                __in_order(root.left)
                print(root.value, root.other_values)
                __in_order(root.right)

        if self.root is not None:
            __in_order(self.root)

    def post_order(self):
        def __post_order(root):
            if root is not None:
                __post_order(root.right)
                print(root.value)
                __post_order(root.left)

        if self.root is not None:
            __post_order(self.root)

    def search(self, value):
        def __search(root, value):
            if root is not None:
                if root.value == value:
                    return root
                elif root.value > value:
                    return __search(root.left, value)
                else:
                    return __search(root.right, value)

        aux = None
        if self.root is not None:
            aux = __search(self.root, value)
        return aux

    def proximity_search(self, value, other_value=None):
        def __search(root, value, other_value):
            if root is not None:
                if value in root.value:
                    if other_value is not None:
                        print(root.value, root.other_values[other_value])
                    else:
                        print(root.value)
                
                __search(root.left, value, other_value)
                __search(root.right, value, other_value)

        aux = None
        if self.root is not None:
            aux = __search(self.root, value, other_value)
        return aux

    def delete(self, value):
        def __replace(root):
            if root.right is None:
                return root.left, root
            else:
                root.right, replace_node = __replace(root.right)
                return root, replace_node

        def __delete(root, value):
            delete_value = None
            deleter_other_values = None
            if root is not None:
                if value < root.value:
                    root.left, delete_value, deleter_other_values = __delete(root.left, value)
                elif value > root.value:
                    root.right, delete_value, deleter_other_values = __delete(root.right, value)
                else:
                    delete_value = root.value
                    deleter_other_values = root.other_values
                    if root.left is None:
                        root = root.right
                    elif root.right is None:
                        root.right = root.left
                    else:
                        root.left, replace_node = __replace(root.left)
                        root.value = replace_node.value
                        root.other_values = replace_node.other_values

                root = self.auto_balance(root)
                self.update_height(root)
            return root, delete_value, deleter_other_values

        delete_value =  None
        deleter_other_values = None
        if self.root is not None:
            self.root, delete_value, deleter_other_values = __delete(self.root, value)
        
        return delete_value, deleter_other_values
    
    def by_level(self):
        tree_queue = Queue()
        if self.root is not None:
            tree_queue.put(self.root)

            while not tree_queue.empty():
                node = tree_queue.get()
                print(node.value)
                if node.left is not None:
                    tree_queue.put(node.left)
                if node.right is not None:
                    tree_queue.put(node.right)

    def height(self, root):
        if root is None:
            return -1
        else:
            return root.height

    def update_height(self, root):
        if root is not None:
            alt_left = self.height(root.left)
            alt_right = self.height(root.right)
            root.height = max(alt_left, alt_right) + 1

    def simple_rotation(self, root, control):
        if control: # RS Right
            aux = root.left
            root.left = aux.right
            aux.right = root
        else: # RS Left
            aux = root.right
            root.right = aux.left
            aux.left = root

        self.update_height(root)
        self.update_height(aux)
        root = aux
        return root

    def double_rotation(self, root, control):
        if control: # RD Right
            root.left = self.simple_rotation(root.left, False)
            root = self.simple_rotation(root, True)
        else:
            root.right = self.simple_rotation(root.right, True)
            root = self.simple_rotation(root, False)
        
        return root

    def auto_balance(self, root):
        if root is not None:
            if self.height(root.left) - self.height(root.right) == 2:
                if self.height(root.left.left) >= self.height(root.left.right):
                    # print("RS RIGHT")
                    root = self.simple_rotation(root, True)
                else:
                    # print("RD RIGHT")
                    root = self.double_rotation(root, True)
            if self.height(root.right) - self.height(root.left) == 2:
                if self.height(root.right.right) >= self.height(root.right.left):
                    # print("RS LEFT")
                    root = self.simple_rotation(root, False)
                else:
                    # print("RD LEFT")
                    root = self.double_rotation(root, False)
        return root

    def count_types(self):
        def __count_types(root):
            if root is not None:
                for t in root.other_values["types"]:
                    if t not in types:
                        types[t] = 1
                    else:
                        types[t] += 1
                __count_types(root.left)
                __count_types(root.right)
        types={}
        if self.root is not None:
            __count_types(self.root)
        return types
                
    def count_heroes(self):
        def __count_heroes(root):
            count = 0
            if root is not None:
                if root.other_values["is_villain"] is False:
                    count += 1
                count += __count_heroes(root.left)
                count += __count_heroes(root.right)

            return count

        total = 0
        if self.root is not None:
            total = __count_heroes(self.root)
        
        return total
    
    def count_nodes(self):
        def __count_nodes(root):
            count=0
            if root is not None:
                count=1
                count+=__count_nodes(root.left)
                count+=__count_nodes(root.right)
            return count
        nodos=0
        if self.root is not None:
            nodos=__count_nodes(self.root)
        return nodos         
    
    def divide_tree(self, arbol_h, arbol_v):
        def __divide_tree(root, arbol_h, arbol_v):
            if root is not None:
                if root.other_values["is_villain"] is False:
                    arbol_h.insert(root.value, root.other_values)
                else:
                    arbol_v.insert(root.value, root.other_values)
                __divide_tree(root.left, arbol_h, arbol_v)
                __divide_tree(root.right, arbol_h, arbol_v)


        __divide_tree(self.root, arbol_h, arbol_v)
    
    def in_order_height(self):
        def __in_order_height(root):
            if root is not None:
                __in_order_height(root.left)
                if root.other_values['height'] > 100:
                    print(root.value, root.other_values['height'])
                __in_order_height(root.right)

        if self.root is not None:
            __in_order_height(self.root)
    
    def in_order_weight(self):
        def __in_order_weight(root):
            if root is not None:
                __in_order_weight(root.left)
                if root.other_values['weight'] < 75:
                    print(root.value, root.other_values['weight'])
                __in_order_weight(root.right)

        if self.root is not None:
            __in_order_weight(self.root)

    def ranking(self, ranking_result):
        def __ranking(root, ranking_result):
            if root is not None:
                __ranking(root.left, ranking_result)
                hero = root.other_values['derrotado_por']
                if hero is not None:
                    if hero not in ranking_result:
                        ranking_result[hero] = 1
                    else:
                        ranking_result[hero] += 1
                __ranking(root.right, ranking_result)

        if self.root is not None:
            __ranking(self.root, ranking_result)

    def greatest_heroes(self):
        rank={}
        self.ranking(rank)
        print(sorted(rank.items(),key=lambda x: x[1],reverse=True)[:3])

    def in_order_villains(self):
        def __in_order(root):
            if root is not None:
                __in_order(root.left)
                if root.other_values["is_villain"] is True:
                    print(root.value, root.other_values)
                __in_order(root.right)

        if self.root is not None:
            __in_order(self.root)

    def starts_with(self, string):
        def __starts_with(root, string):
            if root is not None:
                __starts_with(root.left, string)
                if root.value.startswith(string):
                    print(root.value, root.other_values)
                __starts_with(root.right, string)
        
        if self.root is not None:
            __starts_with(self.root, string)

    def post_order_heroes(self):
        def __post_order(root):
            if root is not None:
                __post_order(root.right)
                if root.other_values["is_villain"] is False:
                    print(root.value)
                __post_order(root.left)

        if self.root is not None:
            __post_order(self.root)        
    
    def in_order_1_value(self,key):
        def __in_order(root,key):
            if root is not None:
                __in_order(root.left,key)
                print(root.value, root.other_values[key])
                __in_order(root.right,key)

        if self.root is not None:
            __in_order(self.root,key)        

    def defeated_by(self, hero):
        def __defeated_by(root, hero):
            if root is not None:
                __defeated_by(root.left,hero)
                if root.other_values["derrotado_por"] ==hero:
                    lista.append(root.value)
                __defeated_by(root.right,hero)

        lista=[]
        if self.root is not None:
            __defeated_by(self.root,hero)
        return lista
    
    def undefeated(self):
        def __undefeated(root):
            if root is not None:
                __undefeated(root.left)
                if root.other_values["derrotado_por"]==None:
                    lista.append(root.value)
                __undefeated(root.right)
        
        lista=[]
        if self.root is not None:
            __undefeated(self.root)
        return lista
    
    def weak_against(self, tipos):
        def __weak_against(root, tipos):
            if root is not None:
                if any(type in root.other_values["weaknesses"] for type in tipos):
                    aux.append(root.value)
                __weak_against(root.left, tipos)
                __weak_against(root.right, tipos)

        aux = []
        if self.root is not None:
            __weak_against(self.root, tipos)
        return aux

    def count_bool(self, key):
        def __count_bool(root,key):
            if root is not None:
                if root.other_values[key] is True:
                    aux[0]+=1
                __count_bool(root.left,key)
                __count_bool(root.right,key)

        aux=[0]
        if self.root is not None:
            __count_bool(self.root,key)
        return aux[0]    