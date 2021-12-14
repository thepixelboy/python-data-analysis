import justpy as jp


def app():
    site = jp.QuasarPage()
    h1 = jp.QDiv(
        a=site,
        text="Analysis of Course Reviews",
        classes="text-h3 text-center q-pa-md",
    )
    p1 = jp.QDiv(a=site, text="This graphs represent course review analysis")

    return site


jp.justpy(app)
