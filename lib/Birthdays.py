from datetime import datetime
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
    def update_name(self,old_name,new_name):
        if old_name not in self.dict.keys():
            raise Exception ("No one found with that name, did you misspell?")
        else:
            self.dict[new_name] = self.dict.pop(old_name)
    def coming_soon(self):
        empty_list = []
        for dates in self.dict.values():
            #formatted = [dates.strftime('%Y-%m-%d')]
            checking = datetime.now() - datetime.strptime(dates,'%d,%m,%Y')
            if checking.days%365 < 30:
                key = next((k for k, v in self.dict.items() if v == dates), None)
                empty_list.append({key,dates[0:5]})
        return empty_list

# Myfriends = Birthdays()
# Myfriends.add("Jasmine","15,06,2003")
# Myfriends.coming_soon()
    