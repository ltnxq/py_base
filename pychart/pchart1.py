from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType

bar = (
    # 使用了InitOpts来初始化图的主题
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    .add_yaxis("商家B", [10, 21, 30, 15, 80, 92])
    # 使用TitleOpts来初始化了标题和子标题
    .set_global_opts(title_opts=opts.TitleOpts(title="Pyecharts练习",subtitle="柱状图"))
)
bar.render_notebook()
