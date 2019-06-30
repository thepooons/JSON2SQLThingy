from flask import Flask, request, jsonify, Blueprint
import pandas as pd
import json #derulo ft. drake
import sys
import importlib
sys.path.append(".")
sys.path.append("..")

GET_blueprint = Blueprint('GET_blueprint', __name__)

@GET_blueprint.route('/<string:table_name>', methods=['GET'])
def show(table_name):
    try:
        from dataHandler2 import table
        return jsonify(table)
    except (ImportError, FileNotFoundError) as e:
        return jsonify([{"no such table": "try again"}])
