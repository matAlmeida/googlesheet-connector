# -*- coding: UTF-8 -*-
# created by Matheus Almeida 2018

import gspread
from flask import Flask, jsonify
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/spreadsheets.readonly']
creds = ServiceAccountCredentials.from_json_keyfile_name('service_secret.json', scope)
client = gspread.authorize(creds)

app = Flask(__name__)

# test
@app.route('/', methods=['GET'])
def hello():

    return "running"

# Returns all entries in a speadsheet by the speadsheet id
# Retorna todas entradas de uma planilha pelo id da planilha
@app.route('/sheet/<string:spreadsheet_id>', methods=['GET'])
def get_sheet_by_id(spreadsheet_id=None):
    sheet = client.open_by_key(spreadsheet_id).sheet1
    info = sheet.get_all_records()

    return jsonify(info)

# Returns all entries in a row of a speadsheet by its id
# Retorna todas as entradas de uma linha de uma planilha pelo seu id
@app.route('/sheet/<string:spreadsheet_id>/row/<string:row>', methods=['GET'])
def get_sheet_row_by_id(spreadsheet_id=None, row=None):
    sheet = client.open_by_key(spreadsheet_id).sheet1
    info = sheet.row_values(row)

    return jsonify(info)

# Returns all the entries in a column of a speadsheet by its id
# Retorna todas as entradas de uma coluna de uma planilha pelo seu id
@app.route('/sheet/<string:spreadsheet_id>/col/<string:col>', methods=['GET'])
def get_sheet_col_by_id(spreadsheet_id=None, col=None):
    sheet = client.open_by_key(spreadsheet_id).sheet1
    info = sheet.col_values(col)

    return jsonify(info)

# Returns the entry of a specific cell in a speadsheet by its id
# Retorna a entrada de uma célula especifica de uma planilha pelo seu id
@app.route('/sheet/<string:spreadsheet_id>/<string:row>/<string:column>', methods=['GET'])
def get_sheet_cell_by_id(spreadsheet_id=None, row=None, column=None):
    sheet = client.open_by_key(spreadsheet_id).sheet1
    info = sheet.cell(row, column).value

    return jsonify(info)

if __name__ == '__main__':
    app.run(debug=True)
