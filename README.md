# Sodifa-Schedule-grabber
Sofia's Public transport scedule web crawler using python.

# Dependencies:
- Selenium (ChromeDriver)
- chromium-browser
- chromium-chromedriver
- Python3
- Pip3

# Installing
> [!WARNING]
> It is recomended to use Linux, because it was build for linux

## Selenium
```
  pip install selenium
```
## For linux (Chromium for web-crawler):
- chromium-browser
```
sudo apt install chromium-browser
```
- chromium-chromedriver
```
sudo apt install chromium-chromedriver
```
## For Windows (Chromium for web-crawler):
- Install chromuim drivers from [here](https://download-chromium.appspot.com/dl/Win_x64?type=snapshots)
- In the python file replace this line:
```
service = Service("/usr/bin/chromedriver")      # !!!Please Change this unless you are in linux
```
With this:
```
service = Service("")      # !!!Please Change this unless you are in linux
```
- in `Command Promt` with elevated privilages install Selemium (Section Installing)

# License
- From [https://www.chromium.org](https://www.chromium.org/Home/)

Except as otherwise [noted](https://developers.google.com/site-policies.html#restrictions), the content of this page is licensed under a [Creative Commons Attribution 2.5 license](https://creativecommons.org/licenses/by/2.5/), and examples are licensed under the [BSD License](https://chromium.googlesource.com/chromium/src/+/HEAD/LICENSE).
