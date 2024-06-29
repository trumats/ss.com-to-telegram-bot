# RSS uz Telegram Bota integrācija

Šis projekts ļauj automātiski saņemt jaunumus no SS.COM transporta sludinājumu RSS plūsmas un nosūtīt tos uz Telegram, filtrējot pēc norādītā cenaskāla.

## Priekšnosacījumi

Pirms projekta palaistīšanas, pārliecinieties, ka jums ir instalēts:
- Python (versija X.X)
- pip (Python pakotņu uzstādīšanas rīks)

## Instalācija

1. **Klonējiet repozitoriju:**

   ```bash
   git clone https://github.com/your-username/rss-telegram-bot.git
   cd rss-telegram-bot

2. **Izveidojiet virtuālo vidi (pēc izvēles, bet ieteicams):**

   ```bash
   python -m venv myenv
   source myenv/bin/activate # Windows operētājsistēmā izmantojiet myenv\Scripts\activate

3. **Instalējiet nepieciešamās atkarības:**
   
   ```bash
   pip install -r requirements.txt

## Konfigurācija

1. **Telegram Bota tokena iestatīšana:**

- Iegūstiet Telegram Bota tokenu no [BotFather](https://t.me/BotFather).
- Aizstājiet `'YOUR_BOT_TOKEN'` ar jūsu īsto Bota tokenu failā `rss_to_telegram.py`.

2. **Telegram čata ID iestatīšana:**

- Iegūstiet savu Telegram čata ID, izmantojot [šo metodi](https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id).
- Aizstājiet `'YOUR_CHAT_ID'` ar jūsu īsto čata ID failā `rss_to_telegram.py`.

## Lietošana

Palaidiet skriptu, lai saņemtu RSS ierakstus un nosūtītu filtrētus ziņojumus uz Telegram:

   ```bash
   python rss_to_telegram.py

Skripts saņems transporta sludinājumu RSS ierakstus no SS.COM un nosūtīs ziņojumus uz jūsu Telegram čatu, filtrējot tos pēc norādītā cenaskāla.

## Pielāgošana

- **Cenu diapazons:**
  - Mainiet `cena_no` un `cena_lidz` mainīgos failā `rss_to_telegram.py`, lai pielāgotu cenu diapazona filtrēšanas kritērijus.

## Piezīmes

- Pārliecinieties, ka jūsu videi ir interneta piekļuve, lai iegūtu RSS plūsmas datus.
- Pielāgojiet skriptu pēc nepieciešamības, atkarībā no jūsu specifiskām prasībām vai RSS plūsmas struktūras.
- Apreķiniet un apstrādājiet jebkādas kļūdas vai izņēmumus, kas var rasties skripta izpildes laikā.
