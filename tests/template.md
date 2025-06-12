##
As a user
So I don't forget the details
I want to keep a record of friends' names and birthdates

As a user
So I can make edits when I've got dates wrong
I want to be able to update a record by passing in a name and new date

As a user
So I can make edits when people change their name
I want to be able to update a record by passing in an old and a new name

As a user
So I can remember to send birthday cards at the right time
I want to be able to list friends whose birthdays are coming up soon and to whom I need to send a card

As a user
So I can buy age-appropriate birthday cards
I want to calculate the upcoming ages for friends with birthdays

##
Verb:Record,Update,Remember,calculate
Noun: Birthdays,Names,list_to_send_birthday_cards,

##
2.
##

Class Birthdays

Methods:

__Init__
self.dict ={}

Add(name,date)
return: nothing
side effect: Name and birthday added to dictionary 

Update_date(name,new_date)
return: nothing
side effect: birthday updated on dictionary 

Update_name(old_name,new_name)
return: nothing
side effect: new_name updated on dictionary 



Coming_soon()
return:List of upcoming birthdays and who they belong to 
side effect:None

Calculate(coming_soon())
return:takes datetime values and calculates the upcoming age
side effect:None


Varibales:
Birthdays.dict = {"Max":20,06,1997,"Paul":"30,04,2002"}
import datetine from datetime
formating: strptime(variable,"%Y,%d,%m")

##
3 Tests
##

## Testing dictionary when adding one name
def test_birthday_name_added_to_dict():
    Myfriends = Birthdays()
    Myfriends.add("Deepaankar","23,09,2003")
    assert myfriends.dict == {"Deepaankar":"23,09,2003"}
## Testing dictionary when adding multiple names
def test_birthday_name_added_to_dict():
    Myfriends = Birthdays()
    friend1 = Myfriends.add("Deepaankar","23,09,2003")
    friend2 = Myfriends.add("Sophie","21,09,2003")
    friend3 = Myfriends.add("James","26,09,2003")
    assert myfriends.dict == ("friend1","friend2","friend3")
## Testing dictionary update method
def test_birthday_date_update
    Myfriends = Birthdays()
    Myfriends.add("Deepaankar","23,09,2003")
    Myfriends.update_date("Deepankar""24,09,2003")
    assert myfriends.dict == {"Deepaankar":"24,09,2003"}
## Trying to update for a name not found
def test_birthday_date_update_misspelled_name():
    Myfriends = Birthdays()
    Myfriends.add("Deepankar","23,09,2003")
    assert Myfriends.update_date("Depankar""24,09,2003") == "No one found with that name, did you misspell?"
## Updating a persons' name
def test_birthday_name_update():
    Myfriends = Birthdays()
    Myfriends.add("Deepaankar","24,09,2003")
    Myfriends.update_name("Deepankar""Daniel")
    assert myfriends.dict == {"Daniel""24,09,2003"}
## Updating persons name but no name found
def test_birthday_name_update_name_not_found():
    Myfriends = Birthdays()
    Myfriends.add("Deepaankar","24,09,2003")
    Myfriends.update_name("Deepankar""Daniel")
    assert Myfriends.update_name("Deepankar""Daniel") == "No one found with that name, did you misspell?"

## Calculate and output a list of whose birthdays from dictionary is coming soon
def test_birthday_coming_soon():
    Myfriends = Birthdays()
    Myfriends.add("Jasmine","15,06,2003")
    assert Myfriends.coming_soon() == [Jasmine,15th June] 
## Calculate and output a list of multiple friends birthdays from dictionary is coming soon excluding those who aren't soon
def test_birthday_coming_soon_multiple():
    Myfriends = Birthdays()
    Myfriends.add("Jasmine","15,06,2003")
    Myfriends.add("Mohammed","18,06,2003")
    Myfriends.add("Harry","15,12,2003")
    assert Myfriends.coming_soon() == [[Jasmine,15th June],[Mohammed,18th June]]
 



    
    

