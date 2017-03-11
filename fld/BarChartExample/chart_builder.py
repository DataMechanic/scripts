
rawDataSet = [
    ['col1','col2','2017-01', '2017-02', '2017-03'],
    ['val1','France'  ,15, 10,  5],
    ['val1','Italy'   , 6, 19, 12],
    ['val1','Spain'   ,20, 10, 18],
    ['val1','Germany' ,17, 11, 15],
    ['val1','Denmark' , 7,  7, 10],
    ['val1','Poland'  ,14, 19,  6],
    ['val1','Swiss'   , 0, 17,  5],
    ['val1','Austria' , 5,  0, 15]]

class Legend:
    colorLegendIterator = -1
    colorLegend = ('RGB(193,57,43)','RGB(45,204,112)','RGB(27,188,155)','RGB(53,152,219)','RGB(155,88,181)','RGB(52,73,94)','RGB(22,160,134)',
                   'RGB(39,174,97)','RGB(42,128,185)','RGB(143,68,173)','RGB(45,62,80)','RGB(241,196,15)','RGB(261,126,35)','RGB(232,76,61)',
                   'RGB(243,156,17)','RGB(210,84,0)','RGB(126,140,141)') # < -- colors
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

    def getLegendHTML(self, startXPoint, chartPadding):
        startYPoint = chartPadding * 3
        lg = ''
        for i in self.chartLegend:
            itemColor = '<circle cx=\'' + str(startXPoint) + '\' cy=\'' + str(startYPoint) + '\' r=\'8\' style=\'fill:' + i['color'] + '\'/>'
            itemName = '<text x=\'' + str(startXPoint + 15) + '\' y=\'' + str(startYPoint + 5) + '\' class=\'legendItems\'>' + i['country'] + '</text>'
            startYPoint += 20
            lg += itemColor + itemName
        return lg

class Bar:
    axisXLabel = 'axisXLabel'
    chartHeight = 500 # ?!!
    barWidth = 80 # const
    barValue = 0
    barStart = 0
    barSegments = []
    def __init__(self, axisXLabel):
        self.axisXLabel = axisXLabel
        self.barSegments = []

    def addSegment(self, country, value, color):
        newSegment = {'country': country, 'value': value, 'color': color}
        self.barSegments.append(newSegment)
        self.barValue += value

    def getBarHTML(self, startXPoint, pxCoefficient=1):
        outputHTML = ''
        axisXLevel = self.chartHeight - 50

        self.barStart = startXPoint + self.barWidth
        barX = self.barStart - self.barWidth / 2
        segmY = axisXLevel
        for i in self.barSegments:
            segmHeight = round( i['value'] * pxCoefficient )
            segmY = segmY - segmHeight
            segment = '<rect x=\'' + str(barX) + '\' y=\'' + str(segmY) + '\' width=\'' + str(self.barWidth) + '\' height=\'' + str(segmHeight) + '\' style=\'fill:' + i['color'] + '\'/>'
            if segmHeight >= 15:
                segmentXLabel = barX + self.barWidth / 2
                segmentYLabel = segmY + 12
                segmentLabelValue = '<text x=\'' + str(segmentXLabel) + '\' y=\'' + str(segmentYLabel) + '\' class=\'barSegmentLabel\'>' + str(i['value']) + '</text>'

                segmentLabelCountry = ''
                if segmHeight >= 30:
                    segmentYLabel += 12
                    segmentLabelCountry = '<text x=\'' + str(segmentXLabel) + '\' y=\'' + str(segmentYLabel) + '\' class=\'barSegmentLabel\'>' + str(i['country']) + '</text>'

                segment = '<g>' + segment + segmentLabelValue + segmentLabelCountry + '</g>'
            outputHTML += segment

        totalXLabel = barX + self.barWidth / 2
        totalYLabel = segmY - 8
        outputHTML += '<text x=\'' + str(totalXLabel) + '\' y=\'' + str(totalYLabel) + '\' class=\'batTotalLabel\'>' + str(self.barValue) + '</text>'

        outputHTML += '<text x=\'' + str(self.barStart) + '\' y=\'' + str(axisXLevel + 15) + '\' class=\'xLabels\'>' + self.axisXLabel + '</text>'
        return outputHTML

class BarChart:
    chartId = 'chartId'
    chartTitle = 'chartTitle'
    dataSet = []

    chartWidth = 600
    chartHeight = 500
    chartMaxValue = 10
    pxCoefficient = 1 # arrange Y axis and data values

    bottomSpace = 50
    leftSpace = 35
    chartPadding = 15 # top & right

    def __init__(self, chartTitle, dataSet, chartId = 'chartId'):
        self.chartId = chartId
        self.chartTitle = chartTitle
        self.dataSet = dataSet

    def createBars(self):
        startPoint = self.leftSpace
        outputHTML = []
        lg = Legend()

        bars = []
        for j in self.dataSet:
            b = Bar(j['timeframe'])
            for i in j['dataset']:
                i['color'] = lg.setColor(i['country'])
                b.addSegment(i['country'], i['value'], i['color'])
            bars.append(b)

            if b.barValue > self.chartMaxValue: self.chartMaxValue = b.barValue

        mV = self.chartMaxValue * 1.1 + 1
        axisYLength = self.chartHeight - self.bottomSpace - self.chartPadding * 3
        pxCoefficient = axisYLength / mV

        for i in bars:
            outputHTML.append( i.getBarHTML(startPoint, pxCoefficient))
            startPoint += b.barWidth * 1.5

        startPoint = self.chartWidth - 150
        outputHTML.append( lg.getLegendHTML(startPoint, self.chartPadding) )

        r = ''.join(outputHTML)
        print(r)
        return r

    def getAxisesHTML(self):
        axises = ''
        xStart = self.leftSpace
        yStart = self.chartHeight - self.bottomSpace

        xEnd = self.chartWidth - self.chartPadding
        yEnd = yStart
        axisX = '<line x1=\'' + str(xStart) + '\' y1=\'' + str(yStart) + '\' x2=\'' + str(xEnd) + '\' y2=\'' + str(yEnd) + '\' style=\'stroke:black; stroke-width:1.5\' />'

        xEnd = xStart
        yEnd = self.chartPadding * 3
        axisY = '<line x1=\'' + str(xStart) + '\' y1=\'' + str(yStart) + '\' x2=\'' + str(xEnd) + '\' y2=\'' + str(yEnd) + '\' style=\'stroke:black; stroke-width:1.5\' />'
        axises = axisX + '\n' + axisY

        axisYLength = yStart - yEnd
        scaleInterval = axisYLength // 3
        labelPositionX = xStart - 4
        for i in range(1,3):
            labelValue = int(self.chartMaxValue * (i/3))
            axises += '<text x=\'' + str(labelPositionX) + '\' y=\'' + str(yStart - scaleInterval * i)+ '\' class=\'yLabels\'>' + str(labelValue) + '</text>'

        print(axises)
        return axises

    def getTitleHTML(self):
        chartTitle = str(self.chartTitle)
        if len(chartTitle) > 40: chartTitle = chartTitle[:37] + '...'
        xStart = self.leftSpace
        yStart = self.chartPadding * 2
        outputTitle = '<text x=\'' + str(xStart) + '\' y=\'' + str(yStart) + '\' class=\'chartTitle\'>' + chartTitle + '</text>'

        print(outputTitle)
        return outputTitle

class DataTransform():

    def transformForBars(self, rawDataSet):
        if len(rawDataSet) < 2:
            return 0

        outputData = []
        header = rawDataSet[0]
        for i in header[2:]:
            outputData.append({'timeframe': i, 'dataset':[]})

        for j in rawDataSet[1:]:
            for key, value in enumerate(outputData):
                item = {'country': j[1], 'value': j[key + 2] }
                value['dataset'].append(item)

        for i in outputData:
            for j in range(0, len(outputData)-1 ):
                if outputData[j]['timeframe'] < outputData[j+1]['timeframe']:
                    v = outputData[j]
                    outputData[j] = outputData[j+1]
                    outputData[j+1] = v

        for bar in outputData:
            for d in reversed(range(0, len(bar['dataset']))):
                for i in range(0, d):
                    if bar['dataset'][i]['value'] < bar['dataset'][i+1]['value']:
                        v = bar['dataset'][i]
                        bar['dataset'][i] = bar['dataset'][i+1]
                        bar['dataset'][i+1] = v

        return outputData

    def getTop(self, rawDataSet, t):
        topValues = []
        for i in rawDataSet:
            r = {'timeframe': i['timeframe'], 'dataset': []}
            cVal = -1
            cIter = 0
            for j in i['dataset']:
                if cVal != j['value']:
                    cIter += 1
                    cVal = j['value']
                if cIter <= t:
                    r['dataset'].append(j)
            topValues.append(r)

        return topValues

class main():
    title = ''
    data = []
    def __init__(self, title, data):
        self.title = title
        self.data = data

        dt = DataTransform()
        self.data = dt.transformForBars(self.data)
        self.data = dt.getTop(self.data, 5)

        ch = BarChart(self.title, self.data)
        ch.createBars()
        ch.getAxisesHTML()
        ch.getTitleHTML()


a = main('some text', rawDataSet)
