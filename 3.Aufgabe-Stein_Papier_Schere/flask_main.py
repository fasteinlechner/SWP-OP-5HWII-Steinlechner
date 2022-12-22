from flask import Flask, render_template, request
from main import get_user_data
app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def hello_world():
    user_data = get_user_data()
    if request.method == "POST":
        username = request.form["username"]
        if username in user_data.keys():
            return render_template('user_statistic.html', user = user_data[username])
        return render_template('user_statistic.html', user="Keine Daten verfügbar!")
    
        
    return render_template('index.html', users = user_data)

if __name__ == '__main__':
    app.run()
    
    
    
