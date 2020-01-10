
resource "kubernetes_pod" "test" {
  metadata {
    name= "flask-api"
     labels = {
          App = "flask-api"
    }

  }

  spec {

        container{
            image= "dockeropticca/sherweb_api:v1"
            name= "flask-api"
            port {
                container_port= 8000
              }

          }


      }
}


resource "kubernetes_service" "apiweb" {
  metadata {
    name = "flask-api"

  }

  spec {
    selector= {
      name = "${kubernetes_pod.test.metadata[0].labels.App}"
    }

    session_affinity = "ClientIP"

    port {
      port        = 80
      target_port = 8000
    }

    type = "LoadBalancer"
  }
}



