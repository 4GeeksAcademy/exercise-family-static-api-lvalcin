
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {
                "id": 1,
                "first_name": "John",
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": 2,
                "first_name": "Jane",
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": 3,
                "first_name": "Jimmy",
                "age": 5,
                "lucky_numbers": [1]
            }
        ]
        self._next_id = 4
# "John Jackson", "Jane Jackson", "Jimmy Jackson"

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        self._members.append(member)
        print(member, "Member is HEREEEEE!!!!!")
        pass

    def delete_member(self, id):
        for member in self._members:
            if member["id"]==id:
                self._members.pop(member)
        # fill this method and update the return
        pass

    def get_member(self, url_id):
        members_list = self._members 
        for member_dictionary in members_list :
            member_id = member_dictionary["id"]
            if url_id == member_id:
                return member_dictionary
    

        # my_list = [1, 2, 3, 4, 5]
        # for item in my_list:
        # print(item)


    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
