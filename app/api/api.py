import time
from flask import Flask, request

app = Flask(__name__)

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
      result = request.form
      print(result)
      rule = []
      trade = {"asset": result["asset"], "quantity" : result["quantity"], "action": result["action"]}
      num_keys = int((len(result)-5)/2)
      for i in range(0, num_keys):
          key = "key" + str(i)
          value = "value" + str(i)
          rule.append((result[key], result[value]))
          print(rule)
    result = {"rule": rule, "trade": trade}
    return result