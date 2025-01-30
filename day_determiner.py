import datetime
import string


class DayDeterminer:
    def determine_day(self) -> string:
        day = datetime.date.today().strftime("%A")
        return day
    
    def calculate_correct_mincha_time(self,time: str) ->str:
        hours, minutes = map(int, time.split(':'))
        if minutes >= 20:
            minutes -= 20
        else:
            offset = 20 - minutes
            minutes = 60 - offset
            hours -= 1
            
        minutes = (minutes // 5) * 5
        new_time = f"{hours}:{minutes:02}"
        return new_time

    def assign_shacharit_info(self,day: str) -> dict:
        shacharit_components = {}
        if day == 'Monday':
            shacharit_components["time"] = "7:30"
            shacharit_components["place"] = "Hillel"
        elif day == 'Tuesday':
            shacharit_components["time"] = "7:30"
            shacharit_components["place"] = "Chabad"
        elif day == 'Wednesday':
            shacharit_components["time"] = "7:30"
            shacharit_components["place"] = "Chabad"
        elif day == 'Thursday':
            shacharit_components["time"] = "7:30"
            shacharit_components["place"] = "Chabad"
        elif day == 'Saturday':
            shacharit_components["time"] = "8:30"
            shacharit_components["place"] = "Hillel"
        elif day == 'Sunday':
            shacharit_components["time"] = "7:30"
            shacharit_components["place"] = "Hillel"
        else: #friday
            print('no need to announce shacharit for tomorrow :)')
        return shacharit_components



def main():
    day_determiner = DayDeterminer()
    current_day = day_determiner.determine_day()
    print(current_day)
    currenttime = datetime.date.today()



if __name__ == "__main__":
    main()
