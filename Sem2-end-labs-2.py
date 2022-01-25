# Yongdong Xi

def open_or_senior(data):
    category = []
    for x in data:
        if x[0]>=55 and x[1]>7:
        # Judge whether the selected element meets two conditions at the same time
            category.append('Senior')
        # Join senior if both requirements are met And record it at the end of the list
        else:
        # If the two requirements are not met at the same time, an 'open' is generated And record it at the end of the list
            category.append('Open')
    return category