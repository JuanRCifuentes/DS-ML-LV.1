from bokeh.plotting import figure, output_file, show

if __name__ == "__main__":
    output_file("simple_graphing.html")
    fig = figure()

    total_vals = int(input('How many values you want to graph?: '))
    x_vals = list(range(-total_vals, total_vals+1))
    y_vals = []

    for i in range(len(x_vals)):
        val = x_vals[i]**2
        y_vals.append(val)

    fig.line(x_vals, y_vals, line_width=2)
    show(fig)