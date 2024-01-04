import json
import os
import mysql.connector

baseFolder = 'C:\\Users\\Public\\Documents\\dev\\self-javascript\\json\\'

def connectDb() -> mysql.connector.connection:
    mytbl = mysql.connector.connect(
        host="",
        port=,
        user="",
        password="",
        database=""
    )
    return mytbl

def insertRec(cnx, data:dict, batch:str):
    with cnx.cursor() as cur:
        sql = 'INSERT INTO practice_result (batch, qId, qNo, objective, isCorrect) VALUES (%s, %s, %s, %s, %s)'
        val = (batch, data['qId'], data['qNo'], data['objective'], data['isCorrect'])
        cur.execute(sql, val)
    #print(cur.rowcount, 'row instered.')


def batchInsertRec(cnx, jsonObj, batch:str):
    for item in jsonObj:
        insertRec(cnx, item, batch)
    cnx.commit()

def parseFile(filePath) -> dict:
    with open(filePath, 'r') as f:
        data = json.load(f)
        return data

def run(mydb):
    cnt = 0
    for filename in os.listdir(baseFolder):
        if filename.endswith('.json') and not filename.startswith('imported-'):
            batch = filename[:15]
            fullFileName = os.path.join(baseFolder, filename)
            jsonObj = parseFile(fullFileName)
            batchInsertRec(mydb, jsonObj, batch)
            newFileName = os.path.join(baseFolder, 'imported-' + filename)
            os.rename(fullFileName, newFileName)
            cnt = cnt + 1
    print(cnt, 'files were imported.')            

with connectDb() as mydb:
    run(mydb)
    #print(connectDb())
