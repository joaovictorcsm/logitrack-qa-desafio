import re
from playwright.sync_api import Page, expect


def test_login_valido(page: Page):
    page.goto("https://logitrack.danieldiegosantana.me/")
    page.fill("#email", "logap@teste.com")
    page.fill("#password", "teste@123")
    page.get_by_role("button", name="Entrar").click()
    page.wait_for_timeout(3000)

    # Deve direcionar para o acesso do sistema
    expect(page).to_have_url(re.compile(".*dashboard.*"))


def test_login_invalido_senha_incorreta(page: Page):
    page.goto("https://logitrack.danieldiegosantana.me/")
    page.fill("#email", "logap@teste.com")
    page.fill("#password", "senhaerrada123")
    page.get_by_role("button", name="Entrar").click()
    page.wait_for_timeout(3000)

    # Não deve permitir acesso ao sistema com senha incorreta
    expect(page).not_to_have_url(re.compile(".*dashboard.*"))


def test_login_invalido_usuario_incorreto(page: Page):
    page.goto("https://logitrack.danieldiegosantana.me/")
    page.fill("#email", "usuarioerrado@teste.com")
    page.fill("#password", "teste@123")
    page.get_by_role("button", name="Entrar").click()
    page.wait_for_timeout(3000)

    # Não deve permitir acesso ao sistema com usuário incorreto
    expect(page).not_to_have_url(re.compile(".*dashboard.*"))