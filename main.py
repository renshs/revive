from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

db_session.global_init("db/mars_explorer.sqlite")

session = db_session.create_session()

user = User()
user.surname = "Scott"
user.name = "Ridley"
user.age = 21
user.position = "captain"
user.speciality = "research engineer"
user.address = "module_1"
user.email = "scott_chief@mars.org"
user.hashed_password = "cap"
session.add(user)

user_1 = User()
user_1.surname = "Kamil"
user_1.name = "Garaev"
user_1.age = 17
user_1.position = "engneer"
user_1.speciality = "research engineer"
user_1.address = "module_1"
user_1.email = "gakamil@mars.org"
user_1.hashed_password = "kam"
session.add(user_1)

user_2 = User()
user_2.surname = "Shama"
user_2.name = "Garip"
user_2.age = 17
user_2.position = "doctor"
user_2.speciality = "surgeon"
user_2.address = "module_2"
user_2.email = "gshama@mars.org"
user_2.hashed_password = "sham"
session.add(user_2)

user_3 = User()
user_3.surname = "Karm"
user_3.name = "Usam"
user_3.age = 14
user_3.position = "farmer"
user_3.speciality = "kolkhoznik"
user_3.address = "module_7"
user_3.email = "karam@mars.org"
user_3.hashed_password = "karm"
session.add(user_3)

session.commit()


def main():
    app.run()


if __name__ == '__main__':
    main()
