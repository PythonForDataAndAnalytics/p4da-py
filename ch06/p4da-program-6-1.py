# Translate Air Quality Index (AQI) from number to color and concern
# https://www.airnow.gov/aqi/aqi-basics/

# lists of levels and corresponding colors and concerns
levels = [301, 201, 151, 101, 51, 0]
colors = ['Maroon', 'Purple', 'Red', 'Orange', 'Yellow', 'Green']
concerns = ['Hazardous', 'Very Unhealthy', 'Unhealthy',
            'Unhealthy for Sensitive Groups', 'Moderate', 'Good']

# input
level = int(input('Enter an AQI level (integer): '))

# processing
for i in range(len(levels)):
    if level >= levels[i]:
        color = colors[i]
        concern = concerns[i]
        break

# output
print('AQI color:', color)
print('AQI concern level:', concern)
