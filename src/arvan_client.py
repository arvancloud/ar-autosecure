import requests
from .config import ARVAN_BASE_URL, DDOS_LEVEL_MAPPING, ARVAN_METRICS_PERIOD


class ArvanClient:
    def __init__(self, api_key, domain):
        self.headers = {'authorization': api_key}
        self.domain = domain

    def change_ddos_level(self, level, ttl=0):
        requests.post(f'{ARVAN_BASE_URL}/domains/{self.domain}/ddos', data={
            'mode': level,
            'ttl': ttl,
        }, headers=self.headers)

    def get_high_request_ips(self):
        return requests.get(
            f'{ARVAN_BASE_URL}/domains/{self.domain}/reports/high-request-ips?period={ARVAN_METRICS_PERIOD}',
            headers=self.headers,
        ).json()['data']

    def block_ip(self, ip):
        requests.post(f'{ARVAN_BASE_URL}/domains/{self.domain}/firewall/rules', data={
            'name': 'High request ip (Auto Block)',
            'action': 'deny',
            'is_enabled': 'true',
            'note': 'Auto Block',
            'sources': [ip],
            'url_pattern': '**',
        }, headers=self.headers)
