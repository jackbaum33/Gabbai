from day_determiner import DayDeterminer
from myzmanim_scraper import myZmanimScraper
from whatsapp_messenger import WhatsappMessenger
import time

class Gabbai:
    def send_mincha_text_to_minyan_chat(self):
        day_determiner = DayDeterminer()
        my_zmanim_scraper = myZmanimScraper()
        whatsapp_messenger = WhatsappMessenger()
        whatsapp_messenger.wait_for_qr_scan()
        shkiyah = my_zmanim_scraper.get_times()["shkiyah"]
        mincha_time = day_determiner.calculate_correct_mincha_time(time=shkiyah)
        print(mincha_time)
        keep = input("continue?")
        body = f"Mincha today is scheduled for {mincha_time} at Hillel"
        print(body)
        whatsapp_messenger.send_text(body=body,name=None,phone_number=None,chat_name="A2Minyan")
    
    def send_shacharit_text_to_minyan_chat(self):
        day_determiner = DayDeterminer()
        whatsapp_messenger = WhatsappMessenger()
        whatsapp_messenger.wait_for_qr_scan()
        shacharit_components = {}
        day = day_determiner.determine_day()
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
        
        body = f"Shacharit tomorrow will be {shacharit_components['time']} at {shacharit_components['place']}"
        print(body)
        time.sleep(5)
        whatsapp_messenger.send_text(body=body,name=None,phone_number=None,chat_name="A2Minyan")

    def text_people_for_shacharit(self, filename: str):
        whatsapp_messenger = WhatsappMessenger()
        whatsapp_messenger.wait_for_qr_scan()
        day_determiner = DayDeterminer()
        shacharit_components = {}
        day = day_determiner.determine_day()
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
        time.sleep(5)
        with open(filename, 'r') as file:
            for line in file:
                info = line.split(',')
                if(info[0]=='name'):
                    continue
                if(info[0]=='end'):
                    time.sleep(1.5)
                    break
                phone_number = info[1]
                name = info[0]
                body = f'hey just a reminder that tomorrow is your day for shacharit, it is taking place at {shacharit_components["time"]} at {shacharit_components["place"]}'
                whatsapp_messenger.send_text(body=body,
                                             name=name,
                                             phone_number=phone_number,
                                             chat_name=None)
                time.sleep(4)


def main():
    gabbai = Gabbai()
    option = input('type m for mincha text, s for shacharit text, r for shacharit reminders (q to quit) (m/s/r/q): ')
    if option == 'm':
        gabbai.send_mincha_text_to_minyan_chat()
    elif option == 'r':
        day_determiner = DayDeterminer()
        day = str(day_determiner.determine_day())
        #will send this text the day before, so <current day> means text everyone
        #for the next day
        if day == 'Monday':
            gabbai.text_people_for_shacharit(filename='tuesday_names.csv')
        elif day == 'Tuesday':
            gabbai.text_people_for_shacharit(filename='wednesday_names.csv')
        elif day == 'Wednesday':
            gabbai.text_people_for_shacharit(filename='thursday_names.csv')
        elif day == 'Thursday':
            gabbai.text_people_for_shacharit(filename='friday_names.csv')
        elif day == 'Saturday':
            gabbai.text_people_for_shacharit(filename='sunday_names.csv')
        elif day == 'sunday':
            gabbai.text_people_for_shacharit(filename='monday_names.csv')
        else: #friday
            print('no need to text people for shabbos davening :)')
        
    elif option == 's':
        gabbai.send_shacharit_text_to_minyan_chat()





if __name__ == '__main__':
    main()