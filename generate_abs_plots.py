import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
# create dummy data for the heatmaps
d1 = pd.read_csv('arxiv_pearson_abs.csv')
d2 = pd.read_csv('arxiv_spearman_abs.csv')
d3 = pd.read_csv('pubmed_pearson_abs.csv')
d4 = pd.read_csv('pubmed_spearman_abs.csv')
data1 = d1.pivot(index = 'dimension', columns = 'metric', values = 'pearson_r')
data2 = d2.pivot(index = 'dimension', columns = 'metric', values = 'spearman_r')
data3 = d3.pivot(index = 'dimension', columns = 'metric', values = 'pearson_r')
data4 = d4.pivot(index = 'dimension', columns = 'metric', values = 'spearman_r')

# generate 4 heatmaps using Seaborn
fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(5, 1)
fig.set_figwidth(24)
fig.set_figheight(36)
ax1.set_aspect('equal')
ax2.set_aspect('equal')
ax3.set_aspect('equal')
ax4.set_aspect('equal')
ax5.set_aspect(0.1)
ax1.set_title(f"Correlation between Human Rating Dimensions and Automatic Metrics for \n Dataset: Arxiv " + "| Value: Pearson R", fontsize = 18)
ax2.set_title(f"Correlation between Human Rating Dimensions and Automatic Metrics for \n Dataset: Arxiv " + "| Value: Spearman R", fontsize = 18)
ax3.set_title(f"Correlation between Human Rating Dimensions and Automatic Metrics for \n Dataset: Pubmed " + "| Value: Pearson R", fontsize = 18)
ax4.set_title(f"Correlation between Human Rating Dimensions and Automatic Metrics for \n Dataset: Pubmed " + "| Value: Spearman R", fontsize = 18)




sns.heatmap(data1, annot= True, cmap = 'Blues', cbar= False, xticklabels= True
            , yticklabels=True, linewidth = 0.5, vmin = 0, vmax = 1, fmt = '.2f',annot_kws={'size' : 16}, ax=ax1)

sns.heatmap(data2, annot= True, cmap = 'Blues', cbar= False, xticklabels= True
            , yticklabels=True, linewidth = 0.5, vmin = 0, vmax = 1, fmt = '.2f',annot_kws={'size' : 16}, ax=ax2)

sns.heatmap(data3,annot= True, cmap = 'Blues', cbar= False,xticklabels= True
            , yticklabels=True, linewidth = 0.5, vmin = 0, vmax = 1, fmt = '.2f',annot_kws={'size' : 16}, ax=ax3)

sns.heatmap(data4,annot= True, cmap = 'Blues', cbar= False, xticklabels= True
            , yticklabels=True, linewidth = 0.5, vmin = 0, vmax = 1, fmt = '.2f', annot_kws={'size' : 16}, ax=ax4)

sns.heatmap(np.zeros((1,1)), cmap="Blues", cbar = True, vmin = 0, vmax = 1, cbar_kws = dict(use_gridspec = False, location = 'bottom'), ax=ax5)
ax5.remove()
# adjust the spacing between subplots

# save the combined heatmaps to an SVG file
fig.savefig("heatmaps_abs.png")
