import logging, json
import pymysql.cursors

from flask import Flask, render_template, request

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


app = Flask('')


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/backend', methods=['GET'])
def test():
    # 0 = Empty parameter  
    
    hwid = request.args.get('hwid')
    
    if hwid or pid == '':
        empty = {
        'error': 'empty',
        'err_code': 0
        }
        return json.dumps(empty)
    
    true = {
     'whitelisted': True,
     'status': 200
    }

    false = {
     'whitelisted': False,
     'status': 401
    }

    
    with connection.cursor() as cursor:
        sql = "SELECT * FROM `hwid` WHERE `hwid`=%s"
        cursor.execute(sql, (hwid))
        result = cursor.fetchone()
        print(result)

    result2 = str(result)

    if hwid not in result2:
      return json.dumps(false), 401
    else:
      return json.dumps(true), 200

@app.errorhandler(404) 
def not_found(e): 
    return render_template("NotFoundError.html"), 404

if __name__ == '__main__':
    app.run(
      host="localhost", 
      port=8080,
      debug=True
    )
