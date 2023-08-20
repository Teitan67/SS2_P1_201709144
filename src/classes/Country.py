class Country:

    def __init__(self,Id,name,location) -> None:
        self.Id=Id
        self.Name=name
        self.Location = location
    
    def sonIguales(self,country)->int:
        if(self.Name==country.Name and self.Location==country.Location):
            return self.Id
        return -1