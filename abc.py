import matplotlib
matplotlib.use('nbagg')

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats
import pandas as pd

sns.set_palette("BuPu_d",desat = 0.6)
sns.set_context("notebook",font_scale = 2.0)

np.random.seed(42424242)

x = stats.gamma(5).rvs(420)
y = stats.gamma(13).rvs(420)

with sns.axes_style("white"):
  sns.jointplot(x,y,kind = "hex",height = 16);
