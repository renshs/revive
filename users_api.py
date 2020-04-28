import flask
from flask import jsonify, request

from data import db_session
from data.users import User

blueprint = flask.Blueprint('users_api', __name__,
                            template_folder='templates')


# @blueprint.route('/api/news')
# def get_news():
#     session = db_session.create_session()
#     users = session.query(User).all()
#     return jsonify(
#         {
#             'users':
#                 [item.to_dict(only=('name', 'about', 'eamil'))
#                  for item in users]
#         }
#     )

@blueprint.route('/api/news')
def get_news():
    return 're'