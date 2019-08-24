# pyAutomationTesting
python3.7 automation test framework(unittest + BeautifulReport+ pytest + pytest-html + selenium)


## 1. Setup Project
```
cd path/to/pyAutomationTesting
pip install -r requirements.txt
```

## 2. Run testcase
```
cd path/to/pyAutomationTesting
python main.py
```

## 3. Add your own testcases
- just add your unittest testcase to cases_unittest dir
- just add your pytest testcase to cases_pytest dir

## 4. Log and Report
- log and report was write in path/to/pyAutomationTesting/result/ if you not set
- unittest report located at: path/to/pyAutomationTesting/result/unittest_report.html
- pytest report located at: path/to/pyAutomationTesting/result/pytest_report.html

## 5. Selenium WebDriver Download for Windows 64 Bit
- [IE WebDriver](http://selenium-release.storage.googleapis.com/index.html): [IEDriverServer.exe](http://selenium-release.storage.googleapis.com/index.html?path=3.9/IEDriverServer_x64_3.9.0.zip)
- [Firefox WebDriver](https://github.com/mozilla/geckodriver/releases): [geckodriver.exe](https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-win64.zip)
- [Chrome WebDriver](http://npm.taobao.org/mirrors/chromedriver): [chromedriver.exe](http://npm.taobao.org/mirrors/chromedriver/77.0.3865.40/chromedriver_win32.zip)
> Extract WebDriver excutable file to C:\WebDriver and then add C:\WebDriver into %PATH%

## 6. Thanks
- [BeautifulReport](https://github.com/TesterlifeRaymond/BeautifulReport)

