{{ importinfo }}
class Context:
    def __init__(self):
        self.states = {{ states }} 
        self.current = self.states[0] 

    def setState(self, index):
        self.current = self.states[index]

if __name__ == "__main__":
    cxt = Context()
    cxt.current.{{ initaction }}(cxt)

