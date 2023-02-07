import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import svgwrite
import time
'''fig_x: plot width
fig_y: plot height
value: data for fill
annotation: labeling for fill
lwidth: line seperation width 
color_map: which color map to use 

''colormaps include: 
    "RdBu": a diverging colormap with red and blue
    "YlOrRd": a sequential colormap with yellow, orange, and red
    "Blues": a sequential colormap with shades of blue
    "Greens": a sequential colormap with shades of green
    "Reds": a sequential colormap with shades of red
    "Oranges": a sequential colormap with shades of orange
    "viridis": a perceptual colormap with green, yellow, and blue hues
    "inferno": a perceptual colormap with red, yellow, and white hues
    "magma": a perceptual colormap with red, yellow, and white hues
''
color_location: colormap legend location
'''

def genplot(d, value, fig_x = 15,
            fig_y = 12, annotations = False, lwidth = 0, color_map = 'Blues',
            color_location = 'bottom', export_as = 'svg', x_ror = 0, y_ror = 0,
            x_axis = 'metric', y_axis = 'dimension', legend = False):
    file = d + '.csv'
    df = pd.read_csv(file)
    pt = df.pivot(index = x_axis, columns = y_axis, values = value)
    plt.figure(figsize=(fig_x, fig_y))
    ax = sns.heatmap(pt, annot= annotations, cmap = color_map, cbar= legend, xticklabels= True
                , yticklabels=True, linewidth = lwidth, vmin = -1, vmax = 1, fmt = '.2f',
                cbar_kws = dict(use_gridspec = False, location = color_location), annot_kws={'size' : 20})
    ax.set_aspect('equal')
    ax.set_title(f"Correlation between Human Rating Dimensions and Automatic Metrics for \n Dataset: {d.capitalize()} " + "| Value: " +(value.replace("_", " ")).capitalize(), fontsize = 36)
    plt.xticks(rotation = x_ror)
    plt.yticks(rotation = y_ror)
    plt.xlabel('Automatic Metrics', fontsize = 24, labelpad = 10)
    plt.ylabel('Human Ratings', fontsize = 24, labelpad = 10)
    plt.savefig(f"{d},{value}.svg")
    plt.show()
colors = ['RdBu', 'YlOrRd', 'Blues', 'Greens', 'Reds', 'Oranges', 'viridis', 'inferno', 'magma', 'coolwarm']


#arxiv plots
genplot('arxiv', 'pearson_r', fig_x = 30, fig_y = 10, x_ror = 0, color_location= 'bottom', color_map= 'Blues',
        x_axis='dimension', y_axis = 'metric', lwidth=0.5, annotations = True, )
genplot('arxiv', 'spearman_r', fig_x = 30, fig_y = 10, x_ror = 0, color_location= 'bottom', color_map = 'Blues',
        x_axis='dimension', y_axis = 'metric', lwidth=0.5, annotations = True)


#pubmed plots
genplot('pubmed', 'pearson_r', fig_x = 30, fig_y = 10, x_ror = 0, color_location= 'bottom', color_map= 'Blues',
        x_axis='dimension', y_axis = 'metric', lwidth=0.5, annotations = True)
genplot('pubmed', 'spearman_r', fig_x = 30, fig_y = 10, x_ror = 0, color_location= 'bottom', color_map = 'Blues',
        x_axis='dimension', y_axis = 'metric', lwidth=0.5, annotations = True, legend = True)
