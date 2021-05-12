from flask import Flask
from flask import jsonify
from flask import Flask,render_template,redirect, url_for, request
from botLogic import BOT
import json
import time
FILENAME="question.csv"

SORRY="SORRY: i can't find question relead to your query u can contact at phone.no:999-999-9999"

#get data ready
filedata=BOT.get_file_data(FILENAME)
datakey=BOT.get_file_data_key2(filedata)
app=Flask(__name__)
def count_Similer(comment_key):
    maxvalue=1
    maxindex=0
    for i in range(0,len(datakey)):
        counthai=BOT.common_member(datakey[i],comment_key)
        if 1 < len(counthai):
            maxindex=i
            maxvalue=len(counthai)
        print(counthai)
    return maxindex,maxvalue

def predict(maxindex,maxvalue):
    if maxvalue!=1:
        return(filedata[maxindex][1])
    else:
        return(SORRY)


@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/',methods=['PUT'])
def get_ans():
    record = json.loads(request.data)
    if record["question"]!="":
        comment_key=record["question"]

        comment_key=BOT.find_keyword(comment_key)
        mi,mv=count_Similer(comment_key)
        datatosend={"replay":predict(mi,mv)}
        time.sleep(0.3)
        return jsonify(posts=datatosend)
    else:
        return jsonify(posts=SORRY)


if __name__ == '__main__':
   app.run(host="localhost",port=5000,debug = True)