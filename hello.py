from flask import Flask
import os

#port = int(os.getenv("PORT"))
#checking if running locally or in cf. if locally assign port 8080 to the webapp
if os.getenv("PORT") is None:
  port = int(8080)
else: 
  port = int(os.getenv("PORT"))
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World! I am running on port ' + str(port)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
