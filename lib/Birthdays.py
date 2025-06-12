class Birthdays():
    def __init__(self):
        self.dict = {}
    def add(self,name,date):
        self.dict.update({name:date})
    def update_date(self,name,new_date):
        if name not in self.dict.keys():
            raise Exception ("No one found with that name, did you misspell?")
        else:
            self.dict.update({name:new_date})
    