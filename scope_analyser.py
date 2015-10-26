__author__ = 'Kaike'

NEW_BLOCK_RULE = 30
END_BLOCK_RULE = 10
IDD_RULE = 29
IDU_RULE = 28

class analyser():
    def __init__(self):
        self.currentLevel = -1
        self.SymbolTable = []
        self.SymbolTableLast = []

    def analize(self, action, token, secundaryToken):
        if action == NEW_BLOCK_RULE:
            self.new_block()

        if action == END_BLOCK_RULE:
            self.end_block()

        if action == IDD_RULE:
            if self.search_in_current_scope(secundaryToken) is not None:
                print("Scope Error. Id already exists")
            else:
                self.define(token)

        if action == IDU_RULE:
            if self.find_by_name(secundaryToken) is None:
                print("Scope Error. Id does not exists")
                self.define(token)



    def new_block(self):
        self.SymbolTable[++self.currentLevel] = None
        self.SymbolTableLast[self.currentLevel] = None
        return self.currentLevel

    def end_block(self):
        return --self.currentLevel

    def define(self, name):
        newObj = {}
        newObj.name = name

        if self.SymbolTable[self.currentLevel] is None:
            self.SymbolTable[self.currentLevel] = newObj
            self.SymbolTableLast[self.currentLevel] = newObj
        else:
            self.SymbolTableLast[self.currentLevel].next = newObj
            self.SymbolTableLast[self.currentLevel] = newObj

        return newObj

    def search_in_current_scope(self, name):
        newObj = self.SymbolTable[self.currentLevel];
        while newObj is not None:
            if newObj.name == name:
                break
            else:
                newObj = newObj.next
        return newObj


    def find_by_name(self, name):
        newObj = {}
        for i in range(self.currentLevel, 0, -1):
            newObj = self.SymbolTable[i]
            while newObj is not None:
                if newObj.name == name:
                    break
                else:
                    newObj = newObj.next
            if newObj is not None:
                break
        return newObj






