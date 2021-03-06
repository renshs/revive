from flask import jsonify
from flask_restful import Resource, reqparse, abort
from data import db_session
from data.users import User


def abort_if_users_not_found(users_id):
    session = db_session.create_session()
    news = session.query(User).get(users_id)
    if not news:
        abort(404, message=f"User {users_id} not found")

test = []

parser = reqparse.RequestParser()
parser.add_argument('name', required=True)
parser.add_argument('email', required=True)
parser.add_argument('about', required=True)
parser.add_argument('hashed_password', required=True)


class UsersResource(Resource):
    def get(selfs, users_id):
        abort_if_users_not_found(users_id)
        session = db_session.create_session()
        users = session.query(User).get(users_id)
        return jsonify({'users': users.to_dict(
            only=('name', 'eamil', 'about',)
        )})

    def delete(self, users_id):
        abort_if_users_not_found(users_id)
        session = db_session.create_session()
        users = session.query(User).get(users_id)
        session.delete(users)
        session.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        try:
            session = db_session.create_session()
            users = session.query(User).all()
            return jsonify({'users': [item.to_dict(
                only=('name', 'eamil', 'about',)) for item in users]
            })
        except Exception as shit:
            test.append(1)

    def post(self):
        args = parser.parse_args()
        print(args['name'], args['email'], args['about'], args['hashed_password'], )
        session = db_session.create_session()
        users = User(
            name=args['name'],
            emal=args['email'],
            about=args['about'],
        )
        users.set_password(args['hashed_password'])
        print(args['name'], args['email'], args['about'], args['hashed_password'], )
        session.add(users)
        session.commit()
        return [jsonify({'success': 'OK'}), args['name'], args['email'], args['about'], args['hashed_password'], ]
print(test)