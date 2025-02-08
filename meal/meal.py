
def main():
    time = input("What time is it? ")
    time = convert(time)
    time = meal_times(time)
    print(time)
    

def convert(time):
    hours, minutes = time.split(":")
    hours =float(hours)  
    minutes = float(minutes)
    total_hours = hours + minutes / 60
    return  total_hours
    

def meal_times(total_hours):

    if total_hours >=  float(7.00) and  total_hours <= float(8.00) :
        return "breakfast time "
    elif total_hours >= float(12.00) and total_hours <= float(13.00) :
        return "lunch time"
    elif total_hours >= float(18.00) and total_hours <= float(19.00):
        return "dinner time "
    else:
        return " "


if __name__ == "__main__":
    main()