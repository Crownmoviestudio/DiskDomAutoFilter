# in & as DiskDom
# Please Don't Remove Credit

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", "1833228")
    API_HASH = os.environ.get("API_HASH", "49ee45ea7c16603385323c0efa03e9ad")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6953751223:AAF0KOM0OZWt4d2-1NrujMqI6h3Ei9S0-D4")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "DiskDomAutoFilterBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002012489202")
    BOT_USERNAME = os.environ.get("DiskDomAutoFilterBot")
    BOT_OWNER = int(os.environ.get("1234011978")
    DATABASE_URL = os.environ.get("")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001911592220")
    ABOUT_BOT_TEXT = """<b> <a href='https://telegram.me/DiskDom'>DiskDom</a> is an open source project.

    Devs: 
        <a href='https://telegram.me/DiskDom'>❤️ DiskDom ❤️</a>
    
    
🤖 My Name: <a href='https://tinyurl.com/DiskDomOfficial'>DiskDom Auto Filter</a>

📝 Language: <a href='https://www.python.org'>Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'>Pyrogram</a>

📡 Server: <a href='https://heroku.com'>Heroku</a>

📡 Server 2: <a href='https://heroku.com'>koyeb</a> <i>comming soon</i>

👨‍💻 Developer Channel: <a href='https://telegram.me/DiskDom'>DiskDom Official</a></b>
"""

    ABOUT_HELP_TEXT = """<b>💋 Developer : <a href='https://telegram.me/DiskDom'>DiskDom</a>

If You Want Your Own Bot Like This Then You Can Contact Our Developer.</b>
"""

    HOME_TEXT = """
<b>Hello Baby ! {}😅,

I'm the one and only fastest URL finder BOT. Add me to any Group and Give me Hunting rights !!

I will be only yours if you will restrict adding me to other groups.
Go to @BotFather to change settings.

Don't be sad ! Your all urls are in safe Hand.

»»» <b>Happy Hunting</b> «««

🔺Thank You <a href='https://telegram.me/DiskDom'>DiskDom</a>🔺 </b>
"""


    START_MSG = """
<b>Hello Baby ! {}😅,

I'm the one and only fastest URL & Post Finder BOT. Add me to any Group and Give me Hunting rights !!

Don't be sad ! Your all urls are in safe Hand.</b>

   »»»» <b>Happy Hunting</b> ««««

🔺 Thank You 🔺 
"""

