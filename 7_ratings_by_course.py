from datetime import datetime

import justpy as jp
import pandas

data = pandas.read_csv("reviews.csv", parse_dates=["Timestamp"])
ratings_by_course = data.groupby(["Course Name"])["Rating"].count()

chart_def = """
{
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie'
    },
    title: {
        text: 'Aggregated Average Ratings by Day of the Week'
    },
    subtitle: {
        text: 'According to the Course Reviews Dataset'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %'
            }
        }
    },
    series: [{
        name: 'Courses',
        colorByPoint: true,
        data: []
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

    hc_data = [
        {
            "name": course_name,
            "y": course_rating,
        }
        for course_name, course_rating in zip(
            ratings_by_course.index, ratings_by_course
        )
    ]
    hc.options.series[0].data = hc_data

    return site


jp.justpy(app)
