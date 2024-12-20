from day_determiner import DayDeterminer
from myzmanim_scraper import myZmanimScraper
from whatsapp_messenger import WhatsappMessenger
import time

class Gabbai:
    def send_mincha_text_to_minyan_chat(self):
        day_determiner = DayDeterminer()
        my_zmanim_scraper = myZmanimScraper()
        #whatsapp_messenger = WhatsappMessenger()
        shkiyah = my_zmanim_scraper.get_times()["shkiyah"]
        mincha_time = day_determiner.calculate_correct_mincha_time(time=shkiyah)
        body = f"Mincha today will be scheduled for {mincha_time}"
        print(body)
        #whatsapp_messenger.send_text(body=body,name=None,phone_number=None,chat_name="A2Minyan")
    
    def text_people_for_shacharit(self, filename: str):
        whatsapp_messenger = WhatsappMessenger()
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
                body = 'hey just a reminder that tomorrow is your day for shacharit'
                whatsapp_messenger.send_text(body=body,
                                             name=name,
                                             phone_number=phone_number,
                                             chat_name=None)


def main():
    gabbai = Gabbai()
    option = input('type m for mincha text, s for shacharit reminder (q to quit) (m/s/q)')
    if option == 'm':
        gabbai.send_mincha_text_to_minyan_chat()
    elif option == 's':
        day_determiner = DayDeterminer()
        day = str(day_determiner.determine_day()).lower()
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






if __name__ == '__main__':
    main()