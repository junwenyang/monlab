from random import randrange

from flask.json import jsonify
from flask import Flask, render_template

from pyecharts import options as opts
from pyecharts.charts import Line

from laoyang.TongYong import getLinuxInfo as gli, hosts_conf as hc


app = Flask(__name__, static_folder="templates")

hostList=hc.getHosts()
ip=hc.getInfoByKey("HOST1","IP")
port=hc.getInfoByKey("HOST1","PORT")
user=hc.getInfoByKey("HOST1","USER")
pwd=hc.getInfoByKey("HOST1","PASS")

hostInfo=hc.setHostInfo("","","",ip,port,user,pwd)

print(hostInfo)

def line_base(hostInfo) -> Line:
    cpu=gli.get_host_status(hostInfo)[0]
    print(cpu)
    line = (
        Line()
        .add_xaxis([1])
        .add_yaxis(
            series_name="CPU使用",
            y_axis=[{cpu}],
            is_smooth=True,
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="监控平台"),
            xaxis_opts=opts.AxisOpts(type_="value"),
            yaxis_opts=opts.AxisOpts(type_="value"),
        )
    )
    return line


@app.route("/")
def index():
    return render_template("mon.html")


@app.route("/lineChart")
def get_line_chart():
    c = line_base(hostInfo)
    return c.dump_options_with_quotes()


idx = 1


@app.route("/lineDynamicData")
def update_line_data():
    cpu=gli.get_host_status(hostInfo)[0]
    global idx
    idx = idx + 1
    print(cpu)
    return jsonify({"name": idx, "value": cpu})


if __name__ == "__main__":
    app.run()