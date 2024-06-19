# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 18:56:24 2024

@author: Giovanny
"""
# pip install seaborn

import pandas as pd
import matplotlib
import seaborn as sns
import io

if __name__ =='__main__':
    from PIL import Image

matplotlib.use('agg')

def regression_plot():
    df = pd.read_csv('tempYearly.csv')
    sns_plot = sns.regplot(x='Rainfall', y='Temperature', data=df)

    image = io.BytesIO()

    sns_plot.figure.savefig(image, format = 'png')

    image.seek(0)
    return image

if __name__ == '__main__':
    image = regression_plot()
    im = Image.open(image)
    im.save('regress.png', 'PNG')
