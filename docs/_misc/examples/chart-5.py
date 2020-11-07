import easychart

#data is a pd.DataFrame about 54k diamonds
data = easychart.datasets.load("diamonds")

#count number of diamonds by cut and color
data = data.groupby(["color", "cut"])["price"].count().unstack()

chart = easychart.new(title="Diamond inventories by cut and color")
chart.categories = data.index
chart.xAxis.title.text = "Diamond color"
chart.yAxis.title.text = "Count"
chart.stacking = "normal"
chart.plot(data, type="column")
chart