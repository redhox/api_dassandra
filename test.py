from cassandra.cluster import Cluster


#cluster = Cluster(['172.27.0.2:9042', '172.27.0.3:9043', '172.27.0.4:9044'])
cluster = Cluster(['cassandra-seed:9042', 'cassandra-node02:9043', 'cassandra-node03:9044'])
session = cluster.connect()
if session == None:
    print("session Null")
else:
    print("session non Null")

# Utilisez la méthode connect pour établir la connexion
session = cluster.connect()
