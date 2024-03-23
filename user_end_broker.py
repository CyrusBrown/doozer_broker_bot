import json
import mongodb_communicator as mongo

database = mongo.Database()

class User:
    def __init__(self, userid, username, level, teststring):
        self.userid = userid
        self.username = username
        self.level = level
        self.teststring = teststring

    def update_db(self):
        database.update_document("users",
                                self.dict_zip(),
                                {'userid': self.userid, "username": self.username, "teststring": self.teststring, "level": self.level})

    def to_json(self):
        return json.dumps(self.__dict__)

    def dict_zip(self):
        userinfo = {}

        for entry in self.__dict__.keys():
            userinfo[entry] = self.__dict__[entry]

        print(userinfo)
        return userinfo
    

    @staticmethod
    def from_json(json_str):
        json_dict = json.loads(json_str)
        return User(json_dict['name'], json_dict['age'])
    
user1 = User(1, "John", 1, "This is a test string")
user1.update_db()