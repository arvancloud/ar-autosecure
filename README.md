# ar-autosecure
Config automatically ArvanCloud Automatic Security Features

### Try it
Running the container:
```
docker run \
 -d \
 -e DOMAIN=example.com \
 -e AUTO_DDOS_PROTECT=true \
 -e AUTO_IP_BLOCK=true \
 -e BLOCK_IP_THRESHOLD=100 \
 -e WHITE_LIST_IPS='1.1.1.1,2.2.2.2' \
 -e HIGH_LOAD_THRESHOLD='80,85,90' \ # off, cookie, javascript, recaptcha
 -e API_KEY=TOKEN_HERE \
 -v /proc/loadavg:/proc/loadavg \
 sadeghhayeri/ar-autosecure:v0.1.0
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
| `HIGH_LOAD_THRESHOLD` | ddos thresholds | string or comma separate list - three number (map to cookie, javascript and recaptcha thresholds) | 80,85,90
| `CHECK_INTERVAL` | check interval (minute) | number | 60
| `BASE_URL` | Arvan base URL | string | https://napi.arvancloud.com/cdn/4.0
| `METRICS_PERIOD` | Arvan report period | enum(1h, 3h, 6h, 12h, 24h, 7d, 30d) | 3h

# Brief
Turn On DDoS Protection if the system load is high
Block High Request IPs in ArvanCloud Firewall


## Capabalities
* Set DDoS Level enable/disable
* Block/Unblock IP in firewall
* Get IP from analytics in CDN

## Useful Link
[CDN API Documentation](https://www.arvancloud.com/docs/api/cdn/4.0)


## Terms and Conditions
* All projects received to ArvanCloud will be reviewed, and the price will be paid to the first approved project.
* All projects have to have test and execution document.
* The project doer has to solve issues and apply required changes for 6 months after approval of the project.
* General changes or changing programming language in each project has to be approved by ArvanCloud.
* In case more than one project is approved by ArvanCLoud, the project fee will be equally divided between winning projects.
* In the evaluation and code reviews stages of a project, no new request for the same project will be accepted. In case the reviewed project fails to pass the quality assessments, the project will be reactivated.
* If projects require any update or edit, merge requests will be accepted in GitHub after reassessment and reapproval.
* Approved projects will be forked in GitHub, and ArvanCloud will star them.
* GitHub name and address of the approved project doer will be published alongside the project. 
