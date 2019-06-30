from flask import Flask, request, jsonify, Blueprint
import pandas as pd
import json #derulo ft. drake
import sys
sys.path.append(".")
sys.path.append("..")

PUT_blueprint = Blueprint('PUT_blueprint2', __name__)

@PUT_blueprint.route('/<string:table>/<int:roll_number_demanded>', methods=['PUT'])
def show(table, roll_number_demanded):
    try:
        from dataHandler2 import table
        matchRow = [i for i in table if i['roll'] == roll_number_demanded]
        result = jsonify(matchRow)
        name = request.get_json(force=True).get('name')
        classBoi = request.get_json(force=True).get('class')
        matchRow[0]['name'] = name
        matchRow[0]['class'] = classBoi
        result = jsonify(table)
    except ImportError:
        result =  jsonify([{"error": 'no such table'}])

    with open('data.json', 'w', encoding = 'utf-8') as outfile:
        json.dump(table, outfile, ensure_ascii=True, indent=2)

    return result
