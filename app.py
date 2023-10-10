from flask import Flask, jsonify
from flask_cassandra import CassandraCluster
from cassandra.cluster import Cluster
app = Flask(__name__)

cluster = Cluster(['172.26.0.2', '172.26.0.2', '172.26.0.3'])
#cluster = Cluster(['172.27.0.2:9042', '172.27.0.3:9043', '172.27.0.4:9044'])
#cluster = Cluster(['cassandra-seed', 'cassandra-node02', 'cassandra-node03'])

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
    result = session.execute(f"SELECT COUNT(*) FROM inspection WHERE idrestaurant = {id}")
    count = result.one()
    return jsonify(count)

@app.route('/restaurants/<string:grade>/top10', methods=['GET'])
def get_top10_restaurants(grade):
    result = session.execute(f"SELECT idrestaurant FROM inspection WHERE grade = '{grade}' LIMIT 10")
    restaurant_ids = result.all()
    restaurant_names = []
    for row in restaurant_ids:
        restaurant_id = row.idrestaurant
        name_result = session.execute(f"SELECT name FROM restaurant WHERE id = {restaurant_id}")
        restaurant_names.append(name_result.one())
    
    return jsonify(restaurant_names)



if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)




