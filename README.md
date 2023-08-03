# http_popup
## Utility
I used it in the pre request script in postman because it does not allow manual inputs and the http server has a 15 minute timeout.

## Build
I used this command to create a binary: `pyinstaller -w -F -i .\popups.ico .\http_popup.py`
I added the binary to RUN -> shell:startup

## Usage
Access it in the browser on localhost
http://localhost:5722/inputs?param1=xxx&param2=xxx

Popup will be created locally like this with numbers of parameters equal to the ones in the request
![image](https://github.com/Tiiberiu/http_popup/assets/12088541/70f1903b-de4a-48f9-af39-27fd435e888c)

After clicking submit a json dict containing the values will be received back
![image](https://github.com/Tiiberiu/http_popup/assets/12088541/57662cf4-a3b4-4204-a28e-93cd8769e9be)

## Mentions
On first reboot it will ask you to allow the http port in firewall, then it will stop

