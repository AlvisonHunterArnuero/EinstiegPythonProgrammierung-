class Client():
    def __init__(self, name, lastname, id: int):
        self.id = id
        self.name = name
        self.lastname = lastname
        
    def __str__(self) -> str:
        return f"id: {self.id} Name: {self.name} LastName: {self.lastname}"
    
print(Client("Alvison", "Hunter", "d"))