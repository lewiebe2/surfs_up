
# 1. import Flask
from flask import Flask

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)

# 3. Define first route for root.
@app.route('/')
def hello_world():
    return 'Hello world'




