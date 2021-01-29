import requests
from .config import ARVAN_BASE_URL, DDOS_LEVEL_MAPPING, ARVAN_METRICS_PERIOD


class ArvanClient:
    def __init__(self, api_key, domain):
        self.headers = {
            'authorization': api_key,
            'content-type': 'application / json;charset = UTF - 8',
            'accept': 'application/json, text/plain, */*',
        }
        self.domain = domain

    def change_ddos_level(self, level, ttl=0):
        print(requests.patch(f'{ARVAN_BASE_URL}/domains/{self.domain}/ddos', json={
            'mode': level,
        }, headers=self.headers).json())

    def get_high_request_ips(self):
        return requests.get(
            f'{ARVAN_BASE_URL}/domains/{self.domain}/reports/high-request-ips?period={ARVAN_METRICS_PERIOD}',
            headers=self.headers,
        ).json()['data']

    def block_ip(self, ip):
        print(requests.post(f'{ARVAN_BASE_URL}/domains/{self.domain}/firewall/rules', json={
            'name': 'High request IP',
            'action': 'deny',
            'is_enabled': True,
            'note': 'Auto Block',
            'sources': [ip],
            'url_pattern': '**',
        }, headers=self.headers).json())

    def get_firewall_rules(self):
        return requests.get(f'{ARVAN_BASE_URL}/domains/{self.domain}/firewall', headers=self.headers).json()['data']

    def is_IP_blocked(self, ip):
        is_blocked = False
        for rule in self.get_firewall_rules()['rules']:
            if rule['action'] == 'deny':
                for source in rule['sources']:
                    if source == ip:
                        is_blocked = True
        return is_blocked