# ar-autosecure
Config automatically ArvanCloud Automatic Security Features

# Brief
Turn On DDoS Protection if the system load is high
Block High Request IPs in ArvanCloud Firewall

## Capabalities
* Set DDoS Level enable/disable
* Block/Unblock IP in firewall
* Get IP from analytics in CDN

### Try it
Running the container:
```
git clone git@github.com:arvancloud/ar-autosecure.git && cd ar-autosecure 
docker build -t ar-autosecure .
docker run \
 -d \
 -e DOMAIN=example.com \
 -e AUTO_DDOS_PROTECT=true \
 -e AUTO_IP_BLOCK=true \
 -e BLOCK_IP_THRESHOLD=100 \
 -e WHITE_LIST_IPS='1.1.1.1,2.2.2.2' \
 -e HIGH_LOAD_THRESHOLD='5,10,50' \
 -e API_KEY='TOKEN_HERE' \
 -v /proc/loadavg:/proc/loadavg \
 ar-autosecure
```

### Config

| Name                                 | Description                                               |  Type | Default
|:-------------------------------------|:----------------------------------------------------------|:-----:|:--------:|
| `API_KEY` | your Arvan API-Key | string | -
| `DOMAIN` | domain | string | -
| `AUTO_DDOS_PROTECT` | enable auto ddos | bool | true
| `AUTO_IP_BLOCK` | enable auto block | bool | true
| `WHITE_LIST_IPS` | white list ips (used for auto block) | string or comma separate list | -
| `BLOCK_IP_THRESHOLD` | request count threshold | number | 1000
| `HIGH_LOAD_THRESHOLD` | ddos thresholds | string or comma separate list - three number (map to cookie, javascript and recaptcha thresholds) | 5,10,50
| `CHECK_INTERVAL` | check interval (seconds) | number | 60
| `BASE_URL` | Arvan base URL | string | https://napi.arvancloud.com/cdn/4.0
| `METRICS_PERIOD` | Arvan report period | enum(1h, 3h, 6h, 12h, 24h, 7d, 30d) | 3h

### 👨🏻‍💻 Contributors:
- SadeghHayeri [![https://github.com/sadeghhayeri](https://img.shields.io/github/followers/sadeghhayeri?color=red&label=Follow&logo=github&style=flat-square)](https://github.com/sadeghhayeri)
