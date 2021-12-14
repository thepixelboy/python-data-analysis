from datetime import datetime

import justpy as jp
import pandas

data = pandas.read_csv("reviews.csv", parse_dates=["Timestamp"])
data["Month"] = data["Timestamp"].dt.strftime("%Y-%m")
month_average_crs = (
    data.groupby(["Month", "Course Name"])["Rating"].count().unstack()
)

chart_def = """
{
    chart: {
        type: 'spline'
    },
    title: {
        text: 'Average Rating by Month by Course'
    },
        subtitle: {
        text: 'According to the Course Reviews Dataset'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 150,
        y: 100,
        floating: true,
        borderWidth: 1,
        backgroundColor:'#FFFFFF'
    },
    xAxis: {
        categories: [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
        ],
        plotBands: [{ // visualize the weekend
            from: 4.5,
            to: 6.5,
            color: 'rgba(68, 170, 213, .2)'
        }]
    },
    yAxis: {
        title: {
            text: 'Fruit units'
        }
    },
    tooltip: {
        shared: true,
        valueSuffix: ' units'
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0.5
        }
    },
    series: [{
        name: 'John',
        data: [3, 4, 3, 5, 4, 10, 12]
    }, {
        name: 'Jane',
        data: [1, 3, 4, 3, 3, 5, 4]
    }]
}
"""


def app():
    site = jp.QuasarPage()
    h1 = jp.QDiv(
        a=site,
        text="Analysis of Course Reviews",
        classes="text-h3 text-center q-pa-md",
    )
    p1 = jp.QDiv(a=site, text="This graphs represent course review analysis")
    hc = jp.HighCharts(a=site, options=chart_def)

    hc.options.xAxis.categories = list(month_average_crs.index)
    hc_data = [
        {
            "name": course_name,
            "data": [
                course_rating
                for course_rating in month_average_crs[course_name]
            ],
        }
        for course_name in month_average_crs.columns
    ]
    hc.options.series = hc_data

    return site


jp.justpy(app)
