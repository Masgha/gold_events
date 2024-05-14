from googletrans import Translator
import json

with open('events.json') as f:
    data = json.load(f)

usd_items = []
for item in data:
    if item['country'] == 'USD':
        usd_items.append(item)

translator = Translator()

items = []
for usd_item in usd_items:
    item = {
        'عنوان' : translator.translate(usd_item['title'], src='en', dest='fa').text,
        'تأثیر' : translator.translate(usd_item['impact'], src='en', dest='fa').text,
        'زمان'  : usd_item['date']
    }
    items.append(item)

with open('test.json', "w", encoding="utf-8") as json_file:
    json.dump(items, json_file, ensure_ascii=False, indent=4)