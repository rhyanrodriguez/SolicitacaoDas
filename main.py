from playwright.sync_api import sync_playwright, Playwright

def onvioAutomation(p: Playwright): 

    browser = p.chromium.launch(headless=False)
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()
    page.goto("https://onvio.com.br/br-portal-do-cliente/service-requesting/general")
    page.click("#trauth-continue-signin-btn")
    page.fill("#username","clara@talst.com.br")
    page.click('//button[contains(text(), "Entrar")]')
    page.fill("#password", "Ma33237518")
    page.click('//button[contains(text(), "Entrar")]')
    page.click('#mfa-reminder-close')
    page.click('#bm-header-app-menu-toggle')

    
    #inserção dos dados para solicitação

    page.click ('#client-combobox-5-input-5-input-5-input-5-input-5-input-5-input-5-input-5-input-5-input')
    page.fill ('#client-combobox-5-input-5-input-5-input-5-input-5-input-5-input-5-input-5-input-5-input', '1428')
    page.click ('//div[contains(text(), "MORETO CONTABILIDADE S/S LTDA")]')
    page.click('#requester')
    page.click('#bui-combobox-list-3-grid-cell-0x0')
    page.click('//label[contains(text(), "OUTRO")]')
    page.click('#department')
    page.click('//div[contains(text(), "Departamento do Sistema")]')
    page.fill('#subject', "Assunto teste")
    page.fill('#description', "Lorem Ipsum")
    page.fill('#due-date', "15032024")

    
    with sync_playwright as p:
        onvioAutomation(p)
    