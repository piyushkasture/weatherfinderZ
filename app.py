from flask import Flask, render_template, request
from location import main as get_weather
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/', methods=['GET','POST'])
def index():
    data = None
    if request.method == 'POST':
        city = request.form['cityName']
        state = request.form['stateName']
        country = request.form['countryName']
        data = get_weather(city, state, country)
        
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)

# app.add_url_rule('/logo.png', redirect_to=url_for('static', filename='logo.png'))
 # debug=True allows for changes to be seen without restarting the server