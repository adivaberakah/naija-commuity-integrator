from flask import Flask, request
from nairaland import post_nairaland
from flask_restplus import Api, Resource, fields

flask_app = Flask(__name__)
app = Api(app = flask_app)

name_space = app.namespace('Topic Creator', description='Creates Topics on Nairaland')
model = app.model('Topic Model', 
				  {'name': fields.String(required = True, 
    					  				 description="Username", help="Name cannot be blank."),
				   'password': fields.String(required = True, 
    					  				 description="Password", help="Password cannot be blank."),
				   'subject': fields.String(required = True, 
    					  				 description="Subject of the Topic", help="Subject cannot be blank."),
				   'body': fields.String(required = True, 
    					  				 description="Body of the Topic", help="Body cannot be blank.") })
@name_space.route("/")
class MainClass(Resource):
	@app.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Error posting content' })
	@app.expect(model)
	def post(self):

		new_post = {
				"name":request.json["name"],
				"password": request.json["password"],
				"subject":request.json["subject"],
				"body":request.json["body"]
			}
    	
		result = post_nairaland(new_post)
		print(result)
		return result

	def get(self):
		return {
			"status": "Got new data"
		}
