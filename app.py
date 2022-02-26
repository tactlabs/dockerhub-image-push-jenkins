from flask import Flask, render_template
from business import get_random_city

app = Flask(__name__)

@app.route('/')
def index():
    random_city = get_random_city()
    result = f'''
    
Your Random City is {random_city}
    
    '''
    return result

app.run(host="0.0.0.0", debug=True)