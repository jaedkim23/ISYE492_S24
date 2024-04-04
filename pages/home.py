from dash import html, register_page  #, callback # If you need callbacks, import it here.
from datetime import date, timedelta
currentDate = date.today()
currentDate_copy = date.today()
May5 = date(2024, 5, 5)
May10 = date(2024, 5, 10)
diff1 = May6 - currentDate
diff2 = May10 - currentDate

mon_count = 0
wed_count = 0

while currentDate_copy <= May5:
    if currentDate_copy.weekday() == 0:  # Monday
        mon_count += 1
    elif currentDate_copy.weekday() == 2:  # Wednesday
        wed_count += 1
    currentDate_copy += timedelta(days=1)

register_page(
    __name__,
    name='Home',
    top_nav=True,
    path='/'
)


def layout():
    layout = html.Div([
        html.H1(
            [
                "Home Page"
            ]
        ),
        html.Div([
            html.H2(
                ['Deadlines:']
            ),
            html.H4(["Today's date: " + str(currentDate)]),
            html.Ul(
                [
                html.Li('Final Presentation to Faculty: May 6th'),
                html.Li('SMSE Engineering/CS Showcase: May 10th'),
                html.Li('Final Presentation to Sponsor: TBD'),
                ]
            ),
            html.H4(['Number of class meetings until May 6th: ' + str(mon_count+wed_count)]),
            html.H4(['Days remaining until May 6th: '  + str(diff1.days)]),
            html.H4(['Days remaining until May 10th: ' + str(diff2.days)]),
            html.H2(
                ['Deliverables']
            ),
            html.Ul(
                [
                html.Li('Final Presentation'),
                html.Li('Final Report'),
                html.Li('All scripts, apps, etc.'),
                html.Li('Showcase Exhibit - Poster + Tool'),
                html.Li('Peer Evaluations'),
                html.Li('Senior Exit Surveys for SMSE')
                ]
            )
        ])
    ])
    return layout