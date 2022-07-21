from multiprocessing.sharedctypes import Value
from pydoc import classname
import dash
from dash import Dash, dcc, html, Input, Output, State, callback
from dash.dependencies import Input, Output, State
from dash import html
from datetime import datetime as dt
import yfinance as yf
import pandas as pd
from pandas.plotting import scatter_matrix
import plotly.express as pk



from matplotlib import container #importing all required modules

app = Dash(__name__)
lbd = html.Div(id="output")
server = app.server
app.layout = html.Div([
    html.P("Welcome to the Stock Dash App!", className="start"),

    html.Div([
        # stock code input
        html.P("Input stock code:"),
        dcc.Input(id='inputstock', type='text', value=''),
        html.Button(id='submit', n_clicks=0, children='Submit'),
        
        
        
    ]),

      

    html.Div([
         # Date range picker input
         dcc.DatePickerRange(id='date', start_date=dt.today(), end_date_placeholder_text='Select a date!'),
         lbd,
         
    ]),

         
    html.Div([
         # Stock price button
         html.Button('Stock Price', id='stock price', n_clicks=0),
         # Indicators button
         html.Button('Indicators', id='indicators', n_clicks=0),
         # Number of days of forecast input
         dcc.Input(id='input days', type='text', placeholder='number of days'),
         #Forecast button
         html.Button('Forecast', id='forcast', n_clicks=0),
         
    ]),

], className='container')




# html.Div([


#     html.Div([
#         #logo
#         #company name
#     ], className = "header"),

#     lbd,
    

    

#     html.Div([
#         #indicator
#     ], id="main-content"),

#     html.Div([
#         #Forecat

#     ], id="forecast")

# ])





           
            




    
                    
    
       

     

                 
         
           
            


               
 
@app.callback(
    Output('output', 'children'),
    Input('submit', 'n_clicks'),
    State('inputstock', 'value'))
    

def update_output(n_clicks, input):
    ticker = yf.Ticker(input)
    inf = ticker.info
    df = pd.DataFrame().from_dict(inf, orient="index").T
    out = df.loc[0].iat[3]


    return '{}'.format(out, n_clicks)   







if __name__ == '__main__':
    app.run_server(debug=True)
