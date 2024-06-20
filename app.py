# -*- coding: utf-8 -*-
#
#Created on Sun Jun 16 10:24:00 2024
#
#@author: Giovanny
#
#
from flask import Flask, send_file
from plotdata import regression_plot
app = Flask(__name__)

@app.route('/', methods=['GET'])
def regr_plot():

    image = regression_plot()

    return send_file(image,
                 download_name='regress.png',
                 mimetype='image/png')
    # return send-file('regplot.png',mimetype='image/png'

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=15000, debug=False)

