from .config import API_KEY, DOMAIN, HIGH_LOAD_THRESHOLD, CHECK_INTERVAL,\
    WHITE_LIST_IPS, BLOCK_IP_THRESHOLD, DDOS_LEVEL_MAPPING, AUTO_IP_BLOCK, AUTO_DDOS_PROTECT
from .arvan_client import ArvanClient
import threading
import os
from time import sleep

arvan_client = ArvanClient(API_KEY, DOMAIN)


def check_load_and_change_ddos_level():
    while True:
        _, load, _ = os.getloadavg()

        if load > HIGH_LOAD_THRESHOLD[2]:
            ddos_level = 3
        elif load > HIGH_LOAD_THRESHOLD[1]:
            ddos_level = 2
        elif load > HIGH_LOAD_THRESHOLD[0]:
            ddos_level = 1
        else:
            ddos_level = 0

        print(f'CURRENT LOAD: {load} -> DDOS_LEVEL: {DDOS_LEVEL_MAPPING[ddos_level]}')
        arvan_client.change_ddos_level(DDOS_LEVEL_MAPPING[ddos_level])
        sleep(CHECK_INTERVAL)


def check_high_requests_ips_and_block():
    while True:
        high_req_ips = arvan_client.get_high_request_ips()
        for row in high_req_ips:
            print('CHECK IP', row['ip'])
            if row['request_count'] > BLOCK_IP_THRESHOLD and row['ip'] not in WHITE_LIST_IPS:
                if not arvan_client.is_IP_blocked(row['ip']):
                    print(f'BLOCK IP {row["ip"]} WITH {row["request_count"]} requests')
                    arvan_client.block_ip(row['ip'])
        sleep(CHECK_INTERVAL)


if __name__ == '__main__':
    if AUTO_IP_BLOCK:
        threading.Thread(target=check_high_requests_ips_and_block).start()
    if AUTO_DDOS_PROTECT:
        threading.Thread(target=check_load_and_change_ddos_level).start()
