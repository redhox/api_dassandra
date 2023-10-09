from flask import Flask, jsonify
from flask_cassandra import CassandraCluster
from cassandra.cluster import Cluster
app = Flask(__name__)

cluster = Cluster(['172.26.0.2', '172.26.0.2', '172.26.0.3'])
session = cluster.connect("resto")

@app.route('/restaurant/')
def get_restaurant_index():
    result = session.execute(f"SELECT * FROM restaurant LIMIT 1;")
    restaurant = result.one()
    return jsonify(restaurant)

@app.route('/restaurant/<int:id>', methods=['GET'])
def get_restaurant(id):
    result = session.execute(f"SELECT * FROM restaurant WHERE id = {id}")
    restaurant = result.one()
    return jsonify(restaurant)

@app.route('/restaurants/<string:cuisine>', methods=['GET'])
def get_restaurants_by_cuisine(cuisine):
    result = session.execute(f"SELECT name FROM restaurant WHERE cuisinetype = '{cuisine}'")
    restaurants = result.all()
    return jsonify(restaurants)

@app.route('/restaurant/<int:id>/inspections', methods=['GET'])
def get_inspections(id):
    result = session.execute(f"SELECT COUNT(*) FROM inspection WHERE restaurant_id = {id}")
    count = result.one()
    return jsonify(count)

@app.route('/restaurants/<string:grade>/top10', methods=['GET'])
def get_top10_restaurants(grade):
    result = session.execute(f"SELECT idrestaurant FROM inspection WHERE grade = '{grade}' LIMIT 10")
    restaurant_ids = result.all()
    
    # Récupérer les noms des restaurants correspondant aux id récupérés
    restaurant_names = []
    for row in restaurant_ids:
        restaurant_id = row.idrestaurant
        name_result = session.execute(f"SELECT name FROM restaurant WHERE id = {restaurant_id}")
        restaurant_names.append(name_result.one())
    
    return jsonify(restaurant_names)



if __name__ == '__main__':
    app.run(debug=True)




