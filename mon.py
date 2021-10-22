from random import randrange
from faker import Faker

from flask.json import jsonify
from flask import Flask, render_template

from pyecharts import options as opts
from pyecharts.charts import Line, Bar, Page
from pyecharts.components import Table

app = Flask(__name__, static_folder="templates")
fk = Faker()

def line_base() -> Line:
    line = (
        Line()
        .add_xaxis(["{}".format(i) for i in range(10)])
        .add_yaxis(
            series_name="",
            y_axis=[randrange(50, 80) for _ in range(10)],
            is_smooth=True,
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="监22控平台"),
            xaxis_opts=opts.AxisOpts(type_="value"),
            yaxis_opts=opts.AxisOpts(type_="value"),
        )
    )
    return line

def bar_base() -> Bar:
    bar = (
        Bar()
        .add_xaxis(['甲','乙'])
        .add_yaxis("A", [randrange(0, 100) for _ in range(2)])
        .add_yaxis("B", [randrange(0, 100) for _ in range(2)])
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"),
            xaxis_opts=opts.AxisOpts(type_="category")
        )
    )
    
    return bar

@app.route("/")
def index():
    return render_template("mon.html")


@app.route("/lineChart")
def get_line_chart():
    c = line_base()
    return c.dump_options_with_quotes()

@app.route("/barChart")
def get_bar_chart():
    c = bar_base()
    return c.dump_options_with_quotes()

idx = 1


@app.route("/lineDynamicData")
def update_line_data():
    global idx
    idx = idx + 1
    return jsonify({"name": idx, "value": randrange(50, 80)})

idx1 = 8
idx2 = 9

@app.route("/barDynamicData")
def update_bar_data():
    global idx1
    idx1 = idx1 + 1
    global idx2
    idx2 = idx2 + 1
    return jsonify({"name": idx1, "value": randrange(50, 80)})

if __name__ == "__main__":
    app.run()