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

    page.hover ('#client-combobox-5-input-5-input-5-input-5-input-5-input-5-input-5-input-5-input-5-input')

   
