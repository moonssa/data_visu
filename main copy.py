from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from data import country_df

stylesheets = [
    "https://cdn.jsdelivr.net/npm/reset-css@5.0.1/reset.min.css",
    "https://fonts.googleapis.com/css2?family=Open+Sans&display=swap",
]
app = Dash(
    __name__, external_stylesheets=stylesheets
)

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
            children=[
                html.H1(
                    "Corona Dashboard",
                    style={"fontSize": "50px"},
                )
            ],
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Table(
                            children=[
                                html.Thead(
                                    children=[
                                        html.Tr(
                                            children=[
                                                html.Th(
                                                    column_name.replace(
                                                        "_",
                                                        " ",
                                                    )
                                                )
                                                for column_name in country_df.columns
                                            ]
                                        )
                                    ]
                                ),
                                html.Tbody(
                                    children=[
                                        html.Tr(
                                            children=[
                                                html.Td(
                                                    value_column
                                                )
                                                for value_column in value
                                            ]
                                        )
                                        for value in country_df.values
                                    ]
                                ),
                            ]
                        )
                    ]
                )
            ]
        ),
    ],
)


if __name__ == "__main__":
    app.run_server(debug=True)
