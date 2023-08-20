class DateTime:

    def __init__(self,Id,Year,Month,Day) -> None:
        self.Id=Id
        self.Year=Year
        self.Month=Month
        self.Day=Day

    def sonIguales(self,fecha) -> int:
        if(self.Year==fecha.Year and self.Month==fecha.Month and  self.Day==fecha.Day):
            return self.Id
        return -1 
   