from dash import Dash, html, dcc


def make_table(df):
    return html.Table(
        children=[
            html.Thead(
                children=[
                    html.Tr(
                        children=[
                            html.Th(
                                col_name.replace(
                                    "_",
                                    " ",
                                )
                            )
                            for col_name in df
                        ]
                    )
                ]
            ),
            html.Tbody(
                children=[
                    html.Tr(
                        children=[
                            html.Td(value_column)
                            for value_column in value
                        ]
                    )
                    for value in df.values
                ]
            ),
        ]
    )
