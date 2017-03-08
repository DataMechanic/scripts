


class Legend:
    colorLegendIterator = -1
    colorLegend = ('red','blue','green', 'grey') # < -- colors
    chartLegend = []

    def setColor(self,countryName):
        isInList = False
        colorName = 'Blank'
        for i in self.chartLegend:
            if countryName == i['country']:
                colorName = i['color']
                isInList = True
                break
        if isInList == False:
            if self.colorLegendIterator < len(self.colorLegend) -1: self.colorLegendIterator += 1
            else: self.colorLegendIterator = 0

            colorName = self.colorLegend[self.colorLegendIterator]
            newCountry = {'country': countryName, 'color': colorName}
            self.chartLegend.append(newCountry)
        return colorName

    def getLegend(self):
        return self.chartLegend

class Bar:
    axisXLabel = 'axisXLabel'
    chartHeight = 500 # ?!!
    barWidth = 80 # const
    barHeight = 0
    barSegments = []
    def __init__(self, axisXLabel):
        self.axisXLabel = axisXLabel

    def addSegment(self, country, value, color):
        newSegment = {'country': country, 'value': value, 'color': color}
        self.barSegments.append(newSegment)
        self.barHeight += value

    def getBarHTML(self, startXPoint, pxCoefficient=1):
        outputHTML = ""
        axisXLevel = self.chartHeight - 50

        barX = startXPoint - self.barWidth / 2
        segmY = axisXLevel
        for i in self.barSegments:
            segmHeight = i['value'] * pxCoefficient
            segmY = segmY - segmHeight
            self.barHeight += segmHeight
            segment = '<rect x=\'' + str(barX) + '\' y=\'' + str(segmY) + '\' width=\'' + str(self.barWidth) + '\' height=\'' + str(segmHeight) + '\' style=\'fill:' + i['color'] + '\'/>'
            outputHTML += segment
        return outputHTML

class BarChart:
    chartId = 'chartId'
    chartTitle = 'chartTitle'

    chartWidth = 500
    chartHeight = 500
    chartMaxValue = 1 # <- ?!!

    bottomSpace = 50
    leftSpace = 35
    chartPadding = 15

    def __init__(self, chartId, chartTitle):
        self.chartId = chartId
        self.chartTitle = chartTitle

    def getAxisesHTML(self):
        axises = ''
        yLength = 0
        xStart = self.leftSpace
        yStart = self.chartHeight - self.bottomSpace

        xEnd = self.chartWidth - self.chartPadding
        yEnd = yStart
        axisX = '<line x1=\'' + str(xStart) + '\' y1=\'' + str(yStart) + '\' x2=\'' + str(xEnd) + '\' y2=\'' + str(yEnd) + '\' style=\'stroke:black; stroke-width:1.5\' />'

        xEnd = xStart
        yEnd = self.chartPadding * 3
        axisY = '<line x1=\'' + str(xStart) + '\' y1=\'' + str(yStart) + '\' x2=\'' + str(xEnd) + '\' y2=\'' + str(yEnd) + '\' style=\'stroke:black; stroke-width:1.5\' />'
        axises = axisX + '\n' + axisY

        yLength = yStart - yEnd
        scaleInterval = yLength // 3
        labelPositionX = xStart - 2
        for i in range(1,3):
            axises += '<text x=\'' + str(labelPositionX) + '\' y=\'' + str(yStart - scaleInterval * i)+ '\' class=\'yLabels\'>' + '00' + '</text>'
        return axises

    def getTitleHTML(self):
        chartTitle = str(self.chartTitle)
        if len(chartTitle) > 40: chartTitle = chartTitle[:37] + '...'
        xStart = self.leftSpace
        yStart = self.chartPadding * 2
        outputTitle = '<text x=\'' + str(xStart) + '\' y=\'' + str(yStart) + '\' class=\'chartTitle\'>' + chartTitle + '</text>'
        return outputTitle



dataSet = [
{'country': 'Italy', 'value': 15},
{'country': 'Spain', 'value': 20},
{'country': 'France', 'value': 25}]
