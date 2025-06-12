from lib.Birthdays import *
import pytest
## Testing dictionary when adding one name
def test_birthday_name_added_to_dict():
    Myfriends = Birthdays()
    Myfriends.add("Deepaankar","23,09,2003")
    assert Myfriends.dict == {"Deepaankar":"23,09,2003"}
# Testing dictionary when adding multiple names
def test_birthday_name_multiple_added_to_dict():
    Myfriends = Birthdays()
    Myfriends.add("Deepaankar","23,09,2003")
    Myfriends.add("Sophie","21,09,2003")
    Myfriends.add("James","26,09,2003")
    assert Myfriends.dict == ({"Deepaankar":"23,09,2003","Sophie":"21,09,2003","James":"26,09,2003"})
## Testing dictionary update method
def test_birthday_date_update():
    Myfriends = Birthdays()
    Myfriends.add("Deepankar","23,09,2003")
    Myfriends.update_date("Deepankar","24,09,2003")
    assert Myfriends.dict == {"Deepankar":"24,09,2003"}
## Trying to update for a name not found
def test_birthday_date_update_misspelled_names():
    Myfriends = Birthdays()
    Myfriends.add("Deepankar","23,09,2003")
    with pytest.raises(Exception) as e:
        Myfriends.update_date("Deepankar1","24,09,2003")
    error_message = str(e.value)
    assert error_message == "No one found with that name, did you misspell?"
# ## Updating a persons' name
# def test_birthday_name_update():
#     Myfriends = Birthdays()
#     Myfriends.add("Deepaankar","24,09,2003")
#     Myfriends.update_name("Deepankar""Daniel")
#     assert myfriends.dict == {"Daniel","24,09,2003"}
# ## Updating persons name but no name found
# def test_birthday_name_update_name_not_found():
#     Myfriends = Birthdays()
#     Myfriends.add("Deepaankar","24,09,2003")
#     Myfriends.update_name("Deepankar""Daniel")
#     assert Myfriends.update_name("Deepankar""Daniel") == "No one found with that name, did you misspell?"

# ## Calculate and output a list of whose birthdays from dictionary is coming soon
# def test_birthday_coming_soon():
#     Myfriends = Birthdays()
#     Myfriends.add("Jasmine","15,06,2003")
#     assert Myfriends.coming_soon() == [Jasmine,15th June] 
# ## Calculate and output a list of multiple friends birthdays from dictionary is coming soon excluding those who aren't soon
# def test_birthday_coming_soon_multiple():
#     Myfriends = Birthdays()
#     Myfriends.add("Jasmine","15,06,2003")
#     Myfriends.add("Mohammed","18,06,2003")
#     Myfriends.add("Harry","15,12,2003")
#     assert Myfriends.coming_soon() == [[Jasmine,15th June],[Mohammed,18th June]]