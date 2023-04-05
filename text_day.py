#Text day program

def text_day (value):
    
    value = int(input("Enter the day of the week (0-6): "))
    
    try:
        if value == 0:
            print("Selected day is", days[value])
        elif value == 1:
            print("Selected day is", days[value])
        elif value == 2:
            print("Selected day is", days[value])
        elif value == 3:
            print("Selected day is", days[value])
        elif value == 4:
            print("Selected day is", days[4])
        elif value == 5:
            print("Selected day is", days[5])
        elif value == 6:
            print("Selected day is", days[6])
        else:
            raise ValueError (value)
        return value
    
    except ValueError:
        print('Value out of bounds (0-6) or negative')

days = ("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday", "Saturday") #tuple
text_day(value=4) #Thursday pops up!
text_day(0) #Sunday pops up!