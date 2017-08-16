import plotly
plotly.tools.set_credentials_file(username='artjur55', api_key='Jq3J3OzkctZFKLAYD4Np')
import numpy

from datetime import datetime

from spreadBot.config import plot_config, plot_figure, plot_format, plot_layout


class Candles:
    def __init__(self, data=None, file=None, name=None, yaxis=None):
        self._plotly = plotly.plotly
        self._figure = plot_figure

        if file:
            self._figure['data'][0]['file'] = file
        if name:
            self._figure['data'][0]['name'] = name
        if yaxis:
            self._figure['data'][0]['yaxis'] = yaxis

        if data:
            self.parse(data)
            # self.plot()

    def parse(self, data=None):
        self.clear()

        if not data:
            return

        for point in data:
            if point[0]: self._figure['data'][0]['x'].append(point[0])
            if point[1]: self._figure['data'][0]['low'].append(point[1])
            if point[2]: self._figure['data'][0]['high'].append(point[2])
            if point[3]: self._figure['data'][0]['open'].append(point[3])
            if point[4]: self._figure['data'][0]['close'].append(point[4])
            if point[5]: self._figure['data'][0]['volume'].append(point[5])

        return self._figure

    def mov_avg(self, interval, window_size=10):
        window = numpy.ones(int(window_size)) / float(window_size)
        return numpy.convolve(interval, window, 'same')

    def apply_mov_avg(self):
        mv_y = self.mov_avg(self._figure['data']['close'])
        mv_x = self._figure['data']['x']
        self._figure['data'].append(dict(x=mv_x, y=mv_y, type='scatter', mode='lines',
                                         line=dict(width=1),
                                         marker=dict(color=plot_config['MOV_AVG_COLOR']),
                                         yaxis='y2', name='Moving Average'))

    def add_vol(self):
        colors = []
        for i in range(len(self._figure['data']['close'])):
            if i != 0:
                if self._figure['data']['close'][i] > self._figure['data']['close'][i - 1]:
                    colors.append(plot_config['INCREASING_COLOR'])
                else:
                    colors.append(plot_config['DECREASING_COLOR'])
            else:
                colors.append(plot_config['DECREASING_COLOR'])
        self._figure['data'].append(dict(x=self._figure['data']['x'],
                                         y=self._figure['data']['volume'],
                                         marker=dict(colors=colors),
                                         type='bar', yaxis='y', name='Volume'))

    def plot(self, mov_avg=False, volume=False):
        if mov_avg:
            self.apply_mov_avg()
        if volume:
            self.add_vol()
        #fig = self._plotly.plot(self._figure, filename=self._figure['data'][0]['file'],
                                #validate=False, fileopt='new')
        self._plotly.image.save_as(self._figure, self._figure['data'][0]['file'], format='png')

    def clear(self):
        self.__init__()
