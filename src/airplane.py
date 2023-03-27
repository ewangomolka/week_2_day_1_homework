
class Airplane:
    def __init__(self, type, crew, flight, glue):
        self.type = type
        self.crew = crew
        self.flight = flight
        self._check_glue = glue 

    def add_member(self, new_member):
        self.crew.append(new_member)

    def check_glue(self):
        return "This is the wrong day to stop sniffing glue"
    
    def has_shirley(self):
        if "Shirley" in self.crew:
            return "Please, call me Shirley"
        else:
            return "Don't call me Shirley"
        
                
    
