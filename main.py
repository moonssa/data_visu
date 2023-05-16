from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from data import country_df, global_df
from builders import make_table


stylesheets = [
    "https://cdn.jsdelivr.net/npm/reset-css@5.0.1/reset.min.css",
    "https://fonts.googleapis.com/css2?family=Open+Sans&display=swap",
]
app = Dash(
    __name__, external_stylesheets=stylesheets
)

map = px.scatter_geo(
    country_df,
    size="Confirmed",
    size_max=50,
    template="plotly_dark",
    locations="Country_Region",
    locationmode="country names",
    color="Confirmed",
    hover_name="Country_Region",
    hover_data={
        "Country_Region": False,
        "Confirmed": ":,2f",
        "Deaths": True,
        "Recovered": True,
    },
)

bar = px.bar(
    global_df,
    x="condition",
    y="count",
    color=["Confirmed", "Deaths", "Recovered"],
    template="plotly_dark",
    title="Global Cases",
    labels={
        "condition": "Condition",
        "count": "Count",
        "color": "Condition",
    },
)
# bar.update_layout(
#     xaxis={"title": "Condition"},
#     yaxis=dict(title="Count"),
# )

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
                        dcc.Graph(figure=map)
                    ]
                ),
                html.Div(
                    children=[
                        dcc.Graph(figure=bar)
                    ]
                ),
                html.Div(
                    children=[
                        make_table(country_df)
                    ]
                ),
            ]
        ),
    ],
)


if __name__ == "__main__":
    app.run_server(debug=True)
