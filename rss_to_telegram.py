import urllib3
import schedule
import time
import feedparser
from bs4 import BeautifulSoup 
from telegram import Bot

# Pārmaini šīs vērtības ar savām
rss_url = 'VĒRTĪBA'
bot_token = 'VĒRTĪBA'
chat_id = 'VĒRTĪBA' 

cena_no = 1
cena_lidz = 1000

sent_entries = set()

def send_messages():
    bot = Bot(token=bot_token)

    while True:
        try:
            feed = feedparser.parse(rss_url)

            for entry in feed.entries:
                entry_id = entry.link  


                if entry_id not in sent_entries:
                    title = entry.title
                    link = entry.link

                    
                    soup = BeautifulSoup(entry.description, 'html.parser')
                    description = soup.get_text(separator='\n')

                
                    price_start_index = description.find("Cena:") 
                    if price_start_index != -1:
                        price_end_index = description.find("€", price_start_index)
                        if price_end_index != -1:
                            price_text = description[price_start_index:price_end_index + 1]
                            
                            price_numeric = ''.join(filter(str.isdigit, price_text))

                           
                            if price_numeric.isdigit():
                                price_value = int(price_numeric)
                                if cena_no <= price_value <= cena_lidz: 
                                    message = f"{title}\n\n{description}\n\nLink: {link}"
                                    bot.send_message(chat_id=chat_id, text=message)
                                    print(f"Message sent for: {title}")
                    sent_entries.add(entry_id)
        except Exception as e:
            print(f"Error: {e}")

        time.sleep(10)
send_messages()