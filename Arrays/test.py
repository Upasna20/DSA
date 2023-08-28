class Test:
    def __init__(self, name):
        self.name = name
        # self.hey()
        
    def hey(self):
        print(f"Hello {self.name}")
        self.obj = Test("Upasna")
        self.obj.hey()
    
test = Test("Upasna")
test.hey()