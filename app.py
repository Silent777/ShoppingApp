from flask import Blueprint
from flask_restful import Api
from resources.Category import CategoryResource
from resources.Comment import CommentResource


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Routes

api.add_resource(CategoryResource, '/Category')
api.add_resource(CommentResource, '/Comment')