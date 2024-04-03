from dash import html, register_page  #, callback # If you need callbacks, import it here.

register_page(
    __name__,
    name='callaway',
    top_nav=True,
    path='/callaway'
)


def layout():
    layout = html.Div([
        html.H1(
            [
                "Callaway"
            ]
        ),
        html.Div([
            html.H2(
                ['Next set of Milestones:']
            ),
            html.Ul(
                [
                    html.Li('Identification of variables that affect quality output measure'),
                    html.Li('Visuals to demonstrate relationship between variables'),
                    html.Li('Summary of data wrangling - how did we subset the data for analysis?'),
                    html.Li('Model to predict failure'),
                    html.Li('Presentation method')
                ]
            )
        ])
    ])
    return layout