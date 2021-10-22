from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType
c = (
     #设置主题
    Pie(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    .add(
        # 系列名称
        "",
        # 系列数据项  格式为 [(key1, value1), (key2, value2)]
        [list(z) for z in zip(Faker.choose(), Faker.values())],
        # 系列 label 颜色  Optional[str]
        color = None,
        # 饼图的半径，数组的第一项是内半径，第二项是外半径
        # 默认设置成百分比，相对于容器高宽中较小的一项的一半
        # Optional[Sequence]
        radius = None,
        # 饼图的中心（圆心）坐标，数组的第一项是横坐标，第二项是纵坐标
        # 默认设置成百分比，设置成百分比时第一项是相对于容器宽度，第二项是相对于容器高度
        # Optional[Sequence]
        center = None,
        # 是否展示成南丁格尔图，通过半径区分数据大小，有'radius'和'area'两种模式。
        # radius：扇区圆心角展现数据的百分比，半径展现数据的大小
        # area：所有扇区圆心角相同，仅通过半径展现数据大小
        # Optional[str]
        rosetype = None,
        # 饼图的扇区是否是顺时针排布。
        is_clockwise = True,
        # 标签配置项，参考 `series_options.LabelOpts`
        label_opts = opts.LabelOpts(),
        # 提示框组件配置项，参考 `series_options.TooltipOpts`
        tooltip_opts = None,
        # 图元样式配置项，参考 `series_options.ItemStyleOpts`
        itemstyle_opts = None,
        # 可以定义 data 的哪个维度被编码成什么。
        # types.Union[types.JSFunc, dict, None]
        encode = None,
        )
    # 全局配置项
    # 设置标题
    .set_global_opts(title_opts=opts.TitleOpts(title="Pie-基本示例"))
    # 系统配置项
    # 设置标签
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("pie_base.html")
)