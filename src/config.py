from decouple import config

API_KEY = config('API_KEY')
DOMAIN = config('DOMAIN')
AUTO_DDOS_PROTECT = config('AUTO_DDOS_PROTECT', default=True, cast=bool)
AUTO_IP_BLOCK = config('AUTO_IP_BLOCK', default=True, cast=bool)
WHITE_LIST_IPS = config('WHITE_LIST_IPS', default='', cast=lambda v: [s.strip() for s in v.split(',')])
BLOCK_IP_THRESHOLD = config('BLOCK_IP_THRESHOLD', default=1000, cast=int)
HIGH_LOAD_THRESHOLD = config('HIGH_LOAD_THRESHOLD', default='80,85,90', cast=lambda v: [int(s.strip()) for s in v.split(',')])
CHECK_INTERVAL = config('CHECK_INTERVAL', default=60, cast=int)
ARVAN_BASE_URL = config('ARVAN_BASE_URL', default='https://napi.arvancloud.com/cdn/4.0')
ARVAN_METRICS_PERIOD = config('ARVAN_METRICS_PERIOD', default='3h')

DDOS_LEVEL_MAPPING = {
    0: 'off',
    1: 'cookie',
    2: 'javascript',
    3: 'recaptcha',
}
