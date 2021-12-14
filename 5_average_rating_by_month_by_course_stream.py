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
        type: 'streamgraph',
        marginBottom: 30,
        zoomType: 'x'
    },
    title: {
        text: 'Average Rating by Month by Course'
    },
        subtitle: {
        text: 'According to the Course Reviews Dataset'
    },

    xAxis: {
        maxPadding: 0,
        type: 'category',
        crosshair: true,
        categories: [],
        labels: {
            align: 'left',
            reserveSpace: false,
            rotation: 270
        },
        lineWidth: 0,
        margin: 20,
        tickWidth: 0
    },

    yAxis: {
        visible: false,
        startOnTick: false,
        endOnTick: false
    },

    legend: {
        enabled: false
    },

    annotations: [],

    plotOptions: {
        series: {
            label: {
                minFontSize: 5,
                maxFontSize: 15,
                style: {
                    color: 'rgba(255,255,255,0.75)'
                }
            }
        }
    },

    // Data parsed with olympic-medals.node.js
    series: [],

    exporting: {
        sourceWidth: 800,
        sourceHeight: 600
    }

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
