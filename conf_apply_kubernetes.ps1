

kubectl apply -f  secret.yaml
kubectl apply -f  mysqldb-service.yaml,mysqldb-deployment.yaml,mysqldb-claim0-persistentvolumeclaim.yaml,flask-api-deployment.yaml,flask-api-service.yaml --overwrite=true