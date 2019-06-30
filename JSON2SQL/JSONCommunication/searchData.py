from flask import Flask, request, jsonify, Blueprint
import pandas as pd
import json #derulo ft. drake
import sys
sys.path.append(".")
sys.path.append("..")

GET_blueprint2 = Blueprint('GET_blueprint2', __name__)

@GET_blueprint2.route('/<string:table>/<int:roll_number_demanded>', methods=['GET'])
def show(table, roll_number_demanded):
    try:
        from dataHandler2 import table
        matchRow = [i for i in table if i['roll'] == roll_number_demanded]
        result = jsonify(matchRow)
        if (matchRow == []):
            result = jsonify([{"error": 'no match in the table'}])

    except ImportError:
        result =  jsonify([{"error": 'no such table'}])

    return result
