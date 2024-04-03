from dash import html, register_page  #, callback # If you need callbacks, import it here.

register_page(
    __name__,
    name='dexcom',
    top_nav=True,
    path='/dexcom'
)


def layout():
    layout = html.Div([
        html.H1(
            [
                "Dexcom"
            ]
        ),
        html.Div([
            html.H2(
                ['Next set of Milestones:']
            ),
            html.Ul(
                [
                    html.Li('Complete formulation of assignment optimization - written out'),
                    html.Li('Tool user interface (UI) design'),
                    html.Li('Tool user workflow map'),
                    html.Li('How are we going to communicate the results?')
                ]
            )
        ])
    ])
    return layout