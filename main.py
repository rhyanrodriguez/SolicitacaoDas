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

    with page.expect_popup() as pi:
        page.goto("https://onvio.com.br/br-portal-do-cliente/service-requesting/general")
    popup = (pi.value)

    sleep (50)


    page.locator('text=Adicionar').click()
    popup.fill('#client-combobox-5-input-5-input-5-input-5-input-5-input-5-input-5-input-5-input-5-input', '1428')
    popup.click('//div[contains(text(), "MORETO CONTABILIDADE S/S LTDA")]')
    popup.click('#requester')
    popup.click('#bui-combobox-list-3-grid-cell-0x0')
    popup.click('//label[contains(text(), "OUTRO")]')
    popup.click('#department')
    popup.click('//div[contains(text(), "Departamento do Sistema")]')
    popup.fill('#subject', "Assunto teste")
    popup.fill('#description', "Lorem Ipsum")
    popup.fill('#due-date', "15032024")

    
with sync_playwright() as p:
    onvioAutomation(p)
    