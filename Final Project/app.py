from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from sqlalchemy import create_engine
import plotly
import pandas as pd
import plotly.express as px
import json
from datetime import datetime

app = Flask(__name__)


## Databse connection 

conn = 'Input your sql database here'

engine = create_engine(conn)
engine.connect()



# route

@app.route("/")
def index():
    ## configuring apple data 
    aapl_data = engine.execute("""
        select distinct * from stocks where symbol = 'aapl' order by date desc;
        """)
    aapl_dataframe = pd.DataFrame(aapl_data,columns=['date','symbol','open','high','low','close','volume'])
    aapl_graph = px.line(aapl_dataframe,x ='date',y= aapl_dataframe.columns[2:6], title='Apple Stocks')
    graph1JSON = json.dumps(aapl_graph, cls = plotly.utils.PlotlyJSONEncoder)

    ## configuring MICROSOFT data
    msft_data = engine.execute("""
        select distinct * from stocks where symbol = 'msft' order by date desc;
        """)
    msft_dataframe = pd.DataFrame(msft_data,columns=['date','symbol','open','high','low','close','volume'])
    msft_graph = px.line(msft_dataframe,x ='date',y= msft_dataframe.columns[2:6], title='Microsoft Stocks')
    graph2JSON = json.dumps(msft_graph, cls = plotly.utils.PlotlyJSONEncoder)

    ## configuring GOOGLE data
    goog_data = engine.execute("""
        select distinct * from stocks where symbol = 'goog' order by date desc;
        """)
    goog_dataframe = pd.DataFrame(goog_data,columns=['date','symbol','open','high','low','close','volume'])
    goog_graph = px.line(goog_dataframe,x ='date',y= goog_dataframe.columns[2:6], title='Google Stocks')
    graph3JSON = json.dumps(goog_graph, cls = plotly.utils.PlotlyJSONEncoder)

    ## configuring TESLA data
    tsla_data = engine.execute("""
        select distinct * from stocks where symbol = 'tsla' order by date desc;
        """)
    tsla_dataframe = pd.DataFrame(tsla_data,columns=['date','symbol','open','high','low','close','volume'])
    tsla_graph = px.line(tsla_dataframe,x ='date',y= tsla_dataframe.columns[2:6], title='Tesla Stocks')
    graph4JSON = json.dumps(tsla_graph, cls = plotly.utils.PlotlyJSONEncoder)

    ## configuring AMAZON data

    amzn_data = engine.execute("""
        select distinct * from stocks where symbol = 'amzn' order by date desc;
        """)
    amzn_dataframe = pd.DataFrame(amzn_data,columns=['date','symbol','open','high','low','close','volume'])
    amzn_graph = px.line(amzn_dataframe,x ='date',y= amzn_dataframe.columns[2:6], title='Amazon Stocks')
    graph5JSON = json.dumps(amzn_graph, cls = plotly.utils.PlotlyJSONEncoder)


    return render_template('home.html',graph1JSON = graph1JSON, graph2JSON = graph2JSON, graph3JSON= graph3JSON, graph4JSON= graph4JSON, graph5JSON=graph5JSON)


#### APPLE #######


@app.route("/aapl")
def aapl():
    ## configuring apple data 
    aapl_data = engine.execute("""
        select distinct * from stocks where symbol = 'aapl' order by date desc;
        """)
    aapl_dataframe = pd.DataFrame(aapl_data,columns=['date','symbol','open','high','low','close','volume'])
    aapl_graph = px.line(aapl_dataframe,x ='date',y= aapl_dataframe.columns[2:6], title='Apple Stocks')
    graph1JSON = json.dumps(aapl_graph, cls = plotly.utils.PlotlyJSONEncoder)
    aapl_data = engine.execute("""
        select distinct * from stocks where symbol = 'aapl' order by date desc;
        """)
    data = tuple(aapl_data.all())
    return render_template('aapl.html', graph1JSON = graph1JSON, data = data)




##### MICROSOFT ########
@app.route("/msft")
def msft():
    ## configuring apple data 
    msft_data = engine.execute("""
        select distinct * from stocks where symbol = 'msft' order by date desc;
        """)
    msft_dataframe = pd.DataFrame(msft_data,columns=['date','symbol','open','high','low','close','volume'])
    msft_graph = px.line(msft_dataframe,x ='date',y= msft_dataframe.columns[2:6], title='Microsoft Stocks')
    graph1JSON = json.dumps(msft_graph, cls = plotly.utils.PlotlyJSONEncoder)
    msft_data = engine.execute("""
        select distinct * from stocks where symbol = 'msft' order by date desc;
        """)
    data = tuple(msft_data.all())
    return render_template('msft.html', graph1JSON = graph1JSON, data = data)


##### GOOGLE ########
@app.route("/goog")
def goog():
    ## configuring apple data 
    goog_data = engine.execute("""
        select distinct * from stocks where symbol = 'goog' order by date desc;
        """)
    goog_dataframe = pd.DataFrame(goog_data,columns=['date','symbol','open','high','low','close','volume'])
    goog_graph = px.line(goog_dataframe,x ='date',y= goog_dataframe.columns[2:6], title='Google Stocks')
    graph1JSON = json.dumps(goog_graph, cls = plotly.utils.PlotlyJSONEncoder)
    goog_data = engine.execute("""
        select distinct * from stocks where symbol = 'goog' order by date desc;
        """)
    data = tuple(goog_data.all())
    return render_template('goog.html', graph1JSON = graph1JSON, data = data)


##### TESLA ########
@app.route("/tsla")
def tsla():
    ## configuring apple data 
    tsla_data = engine.execute("""
        select distinct * from stocks where symbol = 'tsla' order by date desc;
        """)
    tsla_dataframe = pd.DataFrame(tsla_data,columns=['date','symbol','open','high','low','close','volume'])
    tsla_graph = px.line(tsla_dataframe,x ='date',y= tsla_dataframe.columns[2:6], title='Tesla Stocks')
    graph1JSON = json.dumps(tsla_graph, cls = plotly.utils.PlotlyJSONEncoder)
    goog_data = engine.execute("""
        select distinct * from stocks where symbol = 'tsla' order by date desc;
        """)
    data = tuple(goog_data.all())
    return render_template('tsla.html', graph1JSON = graph1JSON, data = data)

##### AMAZON ########
@app.route("/amzn")
def amzn():
    ## configuring apple data 
    amzn_data = engine.execute("""
        select distinct * from stocks where symbol = 'amzn' order by date desc;
        """)
    amzn_dataframe = pd.DataFrame(amzn_data,columns=['date','symbol','open','high','low','close','volume'])
    amzn_graph = px.line(amzn_dataframe,x ='date',y= amzn_dataframe.columns[2:6], title='Amazon Stocks')
    graph1JSON = json.dumps(amzn_graph, cls = plotly.utils.PlotlyJSONEncoder)
    goog_data = engine.execute("""
        select distinct * from stocks where symbol = 'amzn' order by date desc;
        """)
    data = tuple(goog_data.all())
    return render_template('amzn.html', graph1JSON = graph1JSON, data = data)






######################################### API ##############################################

@app.route("/api")
def api():
    ## fetching data
    info = engine.execute("SELECT distinct * FROM stocks;").fetchall()
    api_data = []
    for data in info:
        api_data.append(
            {
                'date':data[0],
                'symbol':data[1],
                'open':data[2],
                'high':data[3],
                'low': data[4],
                'close':data[5],
                'volume':data[6]

            }
        )
    return jsonify(api_data)

@app.route("/api/<symbol>")
def api_id(symbol):
    ## fetching data
    info = engine.execute(f"SELECT distinct * FROM stocks where symbol = '{symbol}' order by date desc;").fetchall()
    api_data = []
    for data in info:
        api_data.append(
            {
                'date': data[0],
                'symbol':data[1],
                'open':data[2],
                'high':data[3],
                'low': data[4],
                'close':data[5],
                'volume':data[6]

            }
        )
    return jsonify(api_data)

@app.route("/<date>")
def api_date(date):
    info = engine.execute(f"SELECT distinct * FROM stocks where date = '{date}'").fetchall()
    api_data = []
    for data in info:
        api_data.append(
            {
                'date': data[0],
                'symbol':data[1],
                'open':data[2],
                'high':data[3],
                'low': data[4],
                'close':data[5],
                'volume':data[6]

            }
        )
    return jsonify(api_data)

@app.route("/<date>/<symbol>")
def api_date_symbol(symbol,date):
    info = engine.execute(f"SELECT distinct * FROM stocks where date = '{date}' and symbol ='{symbol}' ").fetchall()
    api_data = []
    for data in info:
        api_data.append(
            {
                'date': data[0],
                'symbol':data[1],
                'open':data[2],
                'high':data[3],
                'low': data[4],
                'close':data[5],
                'volume':data[6]

            }
        )
    return jsonify(api_data)





if __name__ == '__main__':
    app.run(debug= True)
