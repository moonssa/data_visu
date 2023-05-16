from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

stylesheets = [
    "https://cdn.jsdelivr.net/npm/reset-css@5.0.1/reset.min.css",
    "https://fonts.googleapis.com/css2?family=Open+Sans&display=swap",
]
app = Dash(__name__, external_stylesheets=stylesheets)

app.layout = html.Div(
    style={
        "minHeight": "100vh",
        "backgroundColor": "black",
        "color": "white",
        "fontFamily": "Open Sans serif",
    },
    children=[
        html.Header(
            style={
                "textAlign": "center",
                "paddingTop": "40px",
            },
            children=[html.H1("Corona Dashboard", style={"fontSize": "50px"})],
        )
    ],
)


if __name__ == "__main__":
    app.run_server(debug=True)
