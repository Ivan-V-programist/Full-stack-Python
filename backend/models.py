from config import dataBase

class Contact(dataBase.Model):
    id = dataBase.Column(dataBase.Integer, primary_key=True)
    firstName = dataBase.Column(dataBase.String(50), unique=False, nullable=False)
    LastName = dataBase.Column(dataBase.String(50), unique=False, nullable=False)
    email = dataBase.Column(dataBase.String(100), unique=True, nullable=False)


    def toJson(self):
        return {
            "id": self.id,
            "firstName": self.firstName,
            "lastName": self.LastName,
            "email": self.email
        }