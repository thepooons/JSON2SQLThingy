from flask import Flask, request, jsonify, Blueprint
import pandas as pd
import json #derulo ft. drake
import sys
sys.path.append(".")
sys.path.append("..")


POST_blueprint = Blueprint('POST_blueprint', __name__)

@POST_blueprint.route('/<string:table>/<int:roll_number>', methods=['POST'])
def addData(table, roll_number):
    try:
        from dataHandler2 import table
        name = request.get_json(force=True).get('name')
        classBoi = request.get_json(force=True).get('class')
        dataIn = {'roll': roll_number, 'name': name, 'class': classBoi}
        table.append(dataIn)

    except (ImportError, ) as e:
        table =  [{'roll': roll_number, 'name': name, 'class': classBoi}]

    with open('data.json', 'w', encoding = 'utf-8') as outfile:
        json.dump(table, outfile, ensure_ascii=True, indent=2)

    return jsonify({'added data': table})
#        table = table.reset_index(drop=True)
#        result = json.loads(table.to_json(orient='index'))
