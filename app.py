from dash import *
from testapp import *

app = Dash(__name__)
app.layout = html.Div([
    html.H1('You Passed'),
    github_info_header(),
    html.Img(src="assets/trading.jpg")
])

if __name__ == '__main__':
    app.run_server(debug=True)






