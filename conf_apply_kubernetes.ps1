kubectl apply -f  secret.yaml
kubectl apply -f  mysqldb-deployment.yaml --overwrite=true
kubectl apply -f  mysqldb-service.yaml --overwrite=true
kubectl apply -f  mysqldb-claim0-persistentvolumeclaim.yaml --overwrite=true
kubectl apply -f  flask-api-deployment.yaml --overwrite=true
kubectl apply -f  flask-api-service.yaml --overwrite=true
kubectl expose svc flask-api --type=LoadBalancer --name=titanic-api-service