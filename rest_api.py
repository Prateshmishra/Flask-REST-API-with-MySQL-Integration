from flask import Flask, g , jsonify ,request
from flask_restful import Resource , Api 
import mysql.connector

app = Flask(__name__)
api = Api(app)

# Database configuration
DB_CONFIG = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "Your_mysql_password",
    "database": "flask_api",
}

def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(**DB_CONFIG)
    return g.db

@app.teardown_appcontext
def close_db(error):
    db = g.pop('db', None)
    if db is not None:
        db.close()

class GetAnime(Resource):
    def get(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("select * from anime")
        data = cursor.fetchall()
        return jsonify({"data":data})
    
class AddAnime(Resource):
    def post(self):
        data = request.get_json()

        name = data.get("name")
        genre = data.get("genre")
        episodes = data.get("episodes", 0)
        writer = data.get("writer")                              # to add anime into anime table 
        rating = data.get("rating", 0.0)

        db = get_db()
        cursor = db.cursor()
        query = """INSERT INTO Anime (name, genre, episodes, writer, rating)
                   VALUES (%s, %s, %s, %s, %s)"""
        cursor.execute(query, (name, genre, episodes, writer, rating))
        db.commit()

        
        return jsonify({"message": "Anime added successfully!"})
    
api.add_resource(GetAnime, "/get_data")
api.add_resource(AddAnime,"/add_anime")


if __name__ == "__main__":
    app.run(debug=True)