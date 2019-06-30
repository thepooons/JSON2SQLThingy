from flask import Flask, request, jsonify, Blueprint
import pandas as pd
import json #derulo ft. drake
import sys
sys.path.append(".")
sys.path.append("..")

DELETE_blueprint = Blueprint('DELETE_blueprint2', __name__)

@DELETE_blueprint.route('/<string:table>/<int:roll_number_demanded>', methods=['DELETE'])
def show(table, roll_number_demanded):
    try:
        from dataHandler2 import table
        matchRow = [i for i in table if i['roll'] == roll_number_demanded]
        if (len(matchRow) == 0):
            return jsonify(table)
        table.remove(matchRow[0])
        result = jsonify(table)

    except ImportError:
        result =  jsonify([{"error": 'no such table'}])

    with open('data.json', 'w', encoding = 'utf-8') as outfile:
        json.dump(table, outfile, ensure_ascii=True, indent=2)

    return result
