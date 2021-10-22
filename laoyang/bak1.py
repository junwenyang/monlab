cpu_percent_dict = {}
def cpu():
    # 当前时间
    now = time.strftime('%H:%M:%S', time.localtime(time.time()))
    #  CPU 负载
    cpu_percent = psutil.cpu_percent()
    cpu_percent_dict[now] = cpu_percent
 
 
    # 保持在图表中 10 个数据
    if len(cpu_percent_dict.keys()) == 11:
        cpu_percent_dict.pop(list(cpu_percent_dict.keys())[0])
 
 
def cpu_line() -> Line:
    cpu()
    # 全量更新 pyecharts 图表
    c = (
        Line()
            .add_xaxis(list(cpu_percent_dict.keys()))
            .add_yaxis('', list(cpu_percent_dict.values()), areastyle_opts=opts.AreaStyleOpts(opacity=0.5))
            .set_global_opts(title_opts=opts.TitleOpts(title = now + "CPU负载",pos_left = "center"),
                             yaxis_opts=opts.AxisOpts(min_=0,max_=100,split_number=10,type_="value", name='%'))
    )
    return c
 
 
@app.route("/cpu")
def get_cpu_chart():
    c = cpu_line()
    return c.dump_options_with_quotes()