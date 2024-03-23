import json
import mongodb_communicator as mongo

database = mongo.Database()

class User:
    def __init__(self, userid, username, level, type):
        self.level = level
        self.type = type
        self.userid = userid
        self.username = username

        userids = database.get_consilidated_field("users", "userid", {})

        print(f"Userids: {userids}")

        if self.userid in userids:
            userdoc = database.find_document("users", {"userid": self.userid})
            for entry in self.__dict__.keys():
                print(f"Dict_keys: {self.__dict__.keys()}")
                print(f"Userdoc: {userdoc}")
                self.__dict__[entry] = userdoc[entry]
        


    def update_db(self):
        database.update_document("users",
                                self.dict_zip(),
                                {'userid': self.userid, "username": self.username, "type": self.type, "level": self.level})

    def dict_zip(self):
        userinfo = {}

        for entry in self.__dict__.keys():
            userinfo[entry] = self.__dict__[entry]

        return userinfo
    
    
user1 = User(2, "Bodie", 1, "test_user").update_db()
user2 = User(2, "Altin", 2, "test_user").update_db()
user3 = User(3, "Doozer", 2, "test_user").update_db()
user4 = User(4, "Altin", 2, "test_user").update_db()