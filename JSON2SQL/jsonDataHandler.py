from flask import Flask
from flask import request, jsonify, Response
from flask import Blueprint
from APIs.showTable import GET_blueprint
from APIs.searchData import GET_blueprint2
from APIs.addData import POST_blueprint
from APIs.updateData import PUT_blueprint
from APIs.deleteData import DELETE_blueprint
app = Flask(__name__)

app.register_blueprint(GET_blueprint)
app.register_blueprint(GET_blueprint2)
app.register_blueprint(POST_blueprint)
app.register_blueprint(PUT_blueprint)
app.register_blueprint(DELETE_blueprint)

if __name__ == '__main__':
    app.run(debug = True, port = 8080)
