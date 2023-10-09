from cassandra.cluster import Cluster


cluster = Cluster(['172.26.0.2', '172.26.0.3', '172.26.0.4'])
# Utilisez la méthode connect pour établir la connexion
session = cluster.connect()
