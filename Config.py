import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "13893880"))
    API_HASH = os.environ.get("API_HASH", "16711885d35aa10f66c69031c79c6288")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5842307873:AAHq5CdVQQ-d-zWv7SOD_xpJnsuexfMIlFs")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOHABux7Wwfw0Hbm1VY-xB_BtmEPTlHVTCOH5ILDV2QTa1P136CY3F_Yxi5WrDvVuS_j1C03xY13LDPEvYyXwFH6W_EoQUfXcWXRYodTKdSDXsZWt89f7nlN7OfjKbb3FGQoxynxbTsrUQZibiYyUneJ1n7o2eJrxjfUJwFmgjEE8SSYRfsHi4mmgZhoK6PwTFbHMX022VyX7L3ZzDI_J8DKLFmEdckkWcwWP0Qv-h4GQysCYGTOJoUGOoxEkf7cd-EFRmddwiJEnG5UmjVVoIEiM1OpYuWc-IXkW7HJNhHVLNjouCWm5WwqLuUgUFnGUwllO6aAD0u7tzzvCDGLzOvxbZdA=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "ROLEXX_MUSIC_BOT")
    SUPPORT = os.environ.get("SUPPORT", "ROMEOBOT_OP") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "ROMEO_OP") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/47a9c02d48e24fa6a3a62.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/47a9c02d48e24fa6a3a62.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5166301441")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
