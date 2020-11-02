# Flask Hello World Container
This container is used for the API tasks of the MLP on-site interview.

## How to Run
You can run this flask app by using "flask run --host 0.0.0.0 --port 4000" or you can run this by first building it using "docker build --tag <YOUR TAG> ." and then running "docker run -d -p 4000:4000 --name flask_hw <YOUR TAG>". In order to stop this container, use "docker stop flask_hw". 

### Some Notes
 * If you are running it without Docker, make sure to set the FLASK_APP environment variable to api_app.py. 
 * If you hare using Minikube on windows, make sure to run "minikube docker-env" to use local images.