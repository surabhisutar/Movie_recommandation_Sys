from flask import Flask,request,jsonify
from flask_cors import CORS
import App

app = Flask(__name__)
CORS(app) 
        
@app.route('/movie', methods=['GET'])
def recommend_movies():
    res = App.get_movie_recommendation(request.args.get('title'))
    return jsonify(res)

if __name__=='__main__':
    app.run(port = 5000, debug = True)