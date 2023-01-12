from flask import Flask, redirect
import services
from dash import Dash, dash_table
import dashboard1


app_flask = Flask(__name__)
app_dash = Dash(__name__, server=app_flask, url_base_pathname='/data_dashboard/')
app_dash.layout = dashboard1.get_layout()

@app_flask.route("/")
def start():
    return "Hello"

@app_flask.route("/data")
def get_data():
    df = services.get_wikipedia_data()
    data = df.to_markdown()
    return str(data)

@app_flask.route('/plotly_dashboard') 
def render_dashboard():
    return redirect('/data_dashboard')



if __name__=="__main__":
    app_flask.run()