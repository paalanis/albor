import pytest
import pytest_html
import datetime
from selenium import webdriver
from Repositorio.Scripts.LogIn import *
#from webdriver_auto_update.webdriver_auto_update import WebdriverAutoUpdate
#from webdriver_manager.chrome import ChromeDriverManager

report_name= "test_results_modifi"
report_direct = "C:/Reportes/"

@pytest.fixture(scope="module")
def driver():
        
    driver = webdriver.Chrome()
    return driver
    #yield driver
    #driver.quit()

@pytest.fixture(scope="module",autouse=True)    
def setUp(driver):
    
    #Login(driver).login(T)    
    yield driver    
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--tiempo", action="store")
    
@pytest.fixture(scope='session')
def tiempo(request):
    tiempo = request.config.option.tiempo
    if tiempo is None:
        pytest.skip()
    return tiempo
    
def pytest_html_report_title(report):
    report.title = report_name

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    if not config.option.htmlpath:
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y%m%d_%H%M%S")
        test_name = config.getoption("-k") or report_name
        html_path = f"{report_direct}{test_name}_{timestamp}.html"
        config.option.htmlpath = html_path

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        feature_request = item.funcargs['request']
        driver = feature_request.getfixturevalue('driver')
        #toma una mejor imagen
        S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
        driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment
        driver.find_element(By.TAG_NAME,'body').screenshot('C://Reportes//scr'+timestamp+'.png')
        #driver.save_screenshot('C://Reportes//scr'+timestamp+'.png')
        extra.append(pytest_html.extras.image('file:///C:/Reportes/scr'+timestamp+'.png'))
        #extra.append(pytest_html.extras.image('C:/Screenshots/scr'+timestamp+'.png'))
        # always add url to report
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            extra.append(pytest_html.extras.image('file:///C:/Reportes/scr'+timestamp+'.png'))
            #extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
        report.extras = extra
        