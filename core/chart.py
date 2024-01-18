from pychartjs import BaseChart, ChartType, Color, Options                                  

class MyBarGraph(BaseChart):
    type = ChartType.Bar

    class data:
        label = "Numbers"
        data = [12, 19, 3, 17, 10]
        backgroundColor = Color.Green


class Chart2(BaseChart):
    type = ChartType.Bar

    class labels:
        group = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    class data:

        class apples: 
            data = [2, 8, 11, 7, 2, 4, 3]
            backgroundColor = Color.Palette(Color.Hex('#30EE8090'), 7, 'lightness')
            borderColor = Color.Green
            yAxisID = 'apples'

        class totalEnergy: 
            label = "Total Daily Energy Consumption (kJ)"
            type = ChartType.Line
            data = [5665, 5612, 7566, 8763, 5176, 5751, 6546]
            backgroundColor = Color.RGBA(0,0,0,0)
            borderColor = Color.Purple
            yAxisID = 'totalenergy'

    class options: 

        title = Options.Title("Apples I've eaten compared to total daily energy")

        scales = {
            "yAxes": [
                {"id": "apples",
                 "ticks": {
                     "beginAtZero": True,
                     "callback": "<<function(value, index, values) {return value + ' Big Ones';}>>",
                     }
                },
                {"id": "totalenergy",
                 "position": "right",
                 "ticks": {"beginAtZero": True}
                }
            ]
        }


class ChartLine(BaseChart):

    type = ChartType.Line

    class labels:
        group = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    class data:

        class apples: 
            data = [2, 8, 11, 7, 2, 4, 3]
            backgroundColor = Color.Palette(Color.Hex('#30EE8090'), 7, 'lightness')
            borderColor = Color.Green
            yAxisID = 'apples'

        class totalEnergy: 
            label = "Total Daily Energy Consumption (kJ)"
            type = ChartType.Line
            data = [5665, 5612, 7566, 8763, 5176, 5751, 6546]
            backgroundColor = Color.RGBA(0,0,0,0)
            borderColor = Color.Purple
            yAxisID = 'totalenergy'

    class options: 

        title = Options.Title("Apples I've eaten compared to total daily energy")

        scales = {
            "yAxes": [
                {"id": "apples",
                 "ticks": {
                     "beginAtZero": True,
                     "callback": "<<function(value, index, values) {return value + ' Big Ones';}>>",
                     }
                },
                {"id": "totalenergy",
                 "position": "right",
                 "ticks": {"beginAtZero": True}
                }
            ]
        }
