from playwright.sync_api import sync_playwright, Playwright
from time import sleep

def onvioAutomation(p: Playwright): 

    browser = p.chromium.launch(headless=False)
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()
    page.goto("https://onvio.com.br/#/")
    page.click("#trauth-continue-signin-btn")
    page.fill("#username","clara@talst.com.br")
    page.click('//button[contains(text(), "Entrar")]')
    page.fill("#password", "Ma33237518")
    page.click('//button[contains(text(), "Entrar")]')
    page.click('#mfa-reminder-close')
    page.click('#bm-header-app-menu-toggle')

    #inserção dos dados para solicitação
    page.goto("https://onvio.com.br/br-portal-do-cliente/service-requesting/general")

    page.click('//span[contains(text(), "Adicionar")]')
    sleep (5.5)
   
    page.fill('//*[@id="client-combobox-1-input-1-input"]',"1428")
    page.click('//div[contains(text(), "MORETO CONTABILIDADE S/S LTDA")]')
    page.click('#requester')
    page.click('//div[contains(text(), "Romulo Rodrigues")]')
    page.click('//label[contains(text(), "OUTRO")]')
    page.click('#department')
    page.click('//div[contains(text(), "Departamento do Sistema")]')
    page.fill('#subject', "Assunto teste")
    page.fill('#description', "Lorem Ipsum")
    page.click('//button[contains(text(),"ADICIONAR")]')

    
with sync_playwright() as p:
    onvioAutomation(p)
    