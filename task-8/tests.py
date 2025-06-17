from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

def test_open_homepage(selenium):
    selenium.get("https://practicesoftwaretesting.com")
    WebDriverWait(selenium, 10).until(
        EC.visibility_of_element_located((By.TAG_NAME, "body"))
    )
    body = selenium.find_element(By.TAG_NAME, "body")
    assert body.is_displayed()


def test_header_elements(selenium):
    selenium.get("https://practicesoftwaretesting.com")
    logo = WebDriverWait(selenium, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[title="Practice Software Testing - Toolshop"]')))
    assert logo.is_displayed()
    assert logo.get_attribute("href") == "https://practicesoftwaretesting.com/"
    
    mobile_navbar = selenium.find_element(By.CLASS_NAME, 'navbar-toggler')
    if mobile_navbar.is_displayed():
        mobile_navbar.click()
    
    time.sleep(1)
    
    home_link = selenium.find_element(By.LINK_TEXT, "Home")
    assert home_link.is_displayed()
    assert "nav-link" in home_link.get_attribute("class")
    
    categories_link = selenium.find_element(By.LINK_TEXT, "Categories")
    assert categories_link.is_displayed()
    assert "nav-link" in categories_link.get_attribute("class")
    
    contacts_link = selenium.find_element(By.LINK_TEXT, "Contact")
    assert contacts_link.is_displayed()
    assert "nav-link" in contacts_link.get_attribute("class")
    
    login_link = selenium.find_element(By.LINK_TEXT, "Sign in")
    assert login_link.is_displayed()
    assert "nav-link" in login_link.get_attribute("class")


def test_home_link(selenium):
    selenium.get("https://practicesoftwaretesting.com")
    
    mobile_navbar = selenium.find_element(By.CLASS_NAME, 'navbar-toggler')
    if mobile_navbar.is_displayed():
        mobile_navbar.click()
    
    time.sleep(1)
    
    home_link = selenium.find_element(By.LINK_TEXT, "Home")
    assert "/" in home_link.get_attribute("href")
    home_link.click()
    
    time.sleep(1)
    
    mobile_navbar = selenium.find_element(By.CLASS_NAME, 'navbar-toggler')
    if mobile_navbar.is_displayed():
        filters = selenium.find_element(By.CSS_SELECTOR, '[data-test="filters"]')
        assert filters.is_displayed()
    else:
        home_link = selenium.find_element(By.LINK_TEXT, "Home")
        assert "nav-link active" in home_link.get_attribute("class")


def test_contacts_link(selenium):
    selenium.get("https://practicesoftwaretesting.com")
    
    mobile_navbar = selenium.find_element(By.CLASS_NAME, 'navbar-toggler')
    if mobile_navbar.is_displayed():
        mobile_navbar.click()
    
    time.sleep(1)
    
    contacts_link = selenium.find_element(By.LINK_TEXT, "Contact")
    assert "/contact" in contacts_link.get_attribute("href")
    
    contacts_link.click()
    time.sleep(1)
    
    element = selenium.find_element(By.XPATH, "//h3[text()='Contact']")
    assert element.is_displayed()


def test_login_link(selenium):
    selenium.get("https://practicesoftwaretesting.com")
    
    mobile_navbar = selenium.find_element(By.CLASS_NAME, 'navbar-toggler')
    if mobile_navbar.is_displayed():
        mobile_navbar.click()
    
    time.sleep(1)
    
    login_link = selenium.find_element(By.LINK_TEXT, "Sign in")
    assert "/auth/login" in login_link.get_attribute("href")
    
    login_link.click()
            
    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.XPATH, "//h3[text()='Login']")))
    assert element.is_displayed()


def test_register_link(selenium):
    selenium.get("https://practicesoftwaretesting.com")
    
    mobile_navbar = selenium.find_element(By.CLASS_NAME, 'navbar-toggler')
    if mobile_navbar.is_displayed():
        mobile_navbar.click()
    
    time.sleep(1)
    
    selenium.find_element(By.LINK_TEXT, "Sign in").click()
    
    time.sleep(1)
    selenium.find_element(By.CSS_SELECTOR, '[data-test="register-link"]').click()
            
    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.XPATH, "//h3[text()='Customer registration']")))
    assert element.is_displayed()


def test_forgot_password_link(selenium):
    selenium.get("https://practicesoftwaretesting.com")
    
    mobile_navbar = selenium.find_element(By.CLASS_NAME, 'navbar-toggler')
    if mobile_navbar.is_displayed():
        mobile_navbar.click()
    
    time.sleep(1)
    
    selenium.find_element(By.LINK_TEXT, "Sign in").click()
    
    time.sleep(1)
    selenium.find_element(By.CSS_SELECTOR, '[data-test="forgot-password-link"]').click()
            
    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.XPATH, "//h3[text()='Forgot Password']")))
    assert element.is_displayed()


def test_categories_dropdown(selenium):
    selenium.get("https://practicesoftwaretesting.com")
    
    mobile_navbar = selenium.find_element(By.CLASS_NAME, 'navbar-toggler')
    if mobile_navbar.is_displayed():
        mobile_navbar.click()
    
    time.sleep(1)
    
    categories_button = selenium.find_element(By.CSS_SELECTOR, '[data-test="nav-categories"]')
    categories_button.click()
    
    dropdown = WebDriverWait(selenium, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".navbar-nav > .dropdown > .dropdown-menu")))
    assert dropdown.is_displayed()
    
    hand_tools_link = selenium.find_element(By.CSS_SELECTOR, '[data-test="nav-hand-tools"]')
    assert "Hand Tools" in hand_tools_link.text


def test_hand_tools_link(selenium):
    selenium.get("https://practicesoftwaretesting.com")
    
    mobile_navbar = selenium.find_element(By.CLASS_NAME, 'navbar-toggler')
    if mobile_navbar.is_displayed():
        mobile_navbar.click()
    
    time.sleep(1)
    
    selenium.find_element(By.CSS_SELECTOR, '[data-test="nav-categories"]').click()
    
    time.sleep(1)
    selenium.find_element(By.CSS_SELECTOR, '[data-test="nav-hand-tools"]').click()
    time.sleep(1)
    
    element = selenium.find_element(By.XPATH, "//h2[text()='Category: Hand Tools']")
    assert element.is_displayed()


def test_power_tools_link(selenium):
    selenium.get("https://practicesoftwaretesting.com")
    
    mobile_navbar = selenium.find_element(By.CLASS_NAME, 'navbar-toggler')
    if mobile_navbar.is_displayed():
        mobile_navbar.click()
    
    time.sleep(1)
    
    selenium.find_element(By.CSS_SELECTOR, '[data-test="nav-categories"]').click()
    
    time.sleep(1)
    selenium.find_element(By.CSS_SELECTOR, '[data-test="nav-power-tools"]').click()
    time.sleep(1)
    
    element = selenium.find_element(By.XPATH, "//h2[text()='Category: Power Tools']")
    assert element.is_displayed()


def test_other_link(selenium):
    selenium.get("https://practicesoftwaretesting.com")
    
    mobile_navbar = selenium.find_element(By.CLASS_NAME, 'navbar-toggler')
    if mobile_navbar.is_displayed():
        mobile_navbar.click()
    
    time.sleep(1)
    
    selenium.find_element(By.CSS_SELECTOR, '[data-test="nav-categories"]').click()

    time.sleep(1)
    selenium.find_element(By.CSS_SELECTOR, '[data-test="nav-other"]').click()
    time.sleep(1)
    
    element = selenium.find_element(By.XPATH, "//h2[text()='Category: Other']")
    assert element.is_displayed()


def test_special_tools_link(selenium):
    selenium.get("https://practicesoftwaretesting.com")
    
    mobile_navbar = selenium.find_element(By.CLASS_NAME, 'navbar-toggler')
    if mobile_navbar.is_displayed():
        mobile_navbar.click()
    
    time.sleep(1)
    
    selenium.find_element(By.CSS_SELECTOR, '[data-test="nav-categories"]').click()
    
    time.sleep(1)
    selenium.find_element(By.CSS_SELECTOR, '[data-test="nav-special-tools"]').click()
    time.sleep(1)
    
    element = selenium.find_element(By.XPATH, "//h2[text()='Category: Special Tools']")
    assert element.is_displayed()


def test_rentals_link(selenium):
    selenium.get("https://practicesoftwaretesting.com")
    
    mobile_navbar = selenium.find_element(By.CLASS_NAME, 'navbar-toggler')
    if mobile_navbar.is_displayed():
        mobile_navbar.click()
    
    time.sleep(1)
    
    selenium.find_element(By.CSS_SELECTOR, '[data-test="nav-categories"]').click()
    
    time.sleep(1)
    selenium.find_element(By.CSS_SELECTOR, '[data-test="nav-rentals"]').click()
    time.sleep(1)
    
    element = selenium.find_element(By.XPATH, "//h1[text()='Rentals']")
    assert element.is_displayed()


def test_switch_language_to_german(selenium):
    selenium.get("https://practicesoftwaretesting.com")
    
    mobile_navbar = selenium.find_element(By.CLASS_NAME, 'navbar-toggler')
    if mobile_navbar.is_displayed():
        mobile_navbar.click()
    
    time.sleep(1)
    
    selenium.find_element(By.CSS_SELECTOR, '[data-test="language-select"]').click()
    selenium.find_element(By.CSS_SELECTOR, '[data-test="lang-de"]').click()

    time.sleep(1)
    
    assert "DE" in selenium.find_element(By.CSS_SELECTOR, '[data-test="language-select"]').text
    assert "Sortieren" in selenium.page_source
    assert "Preisspanne" in selenium.page_source
    assert "Suche" in selenium.page_source
    assert "Nach Kategorie" in selenium.page_source
    assert "Nach Marken" in selenium.page_source
    assert "Kategorien" in selenium.page_source
    assert "Kontakt" in selenium.page_source
    assert "Einloggen" in selenium.page_source


def test_switch_language_to_english(selenium):
    selenium.get("https://practicesoftwaretesting.com")
    
    mobile_navbar = selenium.find_element(By.CLASS_NAME, 'navbar-toggler')
    if mobile_navbar.is_displayed():
        mobile_navbar.click()
    
    time.sleep(1)
    
    selenium.find_element(By.CSS_SELECTOR, '[data-test="language-select"]').click()
    selenium.find_element(By.CSS_SELECTOR, '[data-test="lang-en"]').click()

    time.sleep(1)
    
    assert "EN" in selenium.find_element(By.CSS_SELECTOR, '[data-test="language-select"]').text
    assert "Sort" in selenium.page_source
    assert "Price Range" in selenium.page_source
    assert "Search" in selenium.page_source
    assert "By category" in selenium.page_source
    assert "By brand" in selenium.page_source
    assert "Categories" in selenium.page_source
    assert "Contact" in selenium.page_source
    assert "Sign in" in selenium.page_source


def test_switch_language_to_spanish(selenium):
    selenium.get("https://practicesoftwaretesting.com")
    
    mobile_navbar = selenium.find_element(By.CLASS_NAME, 'navbar-toggler')
    if mobile_navbar.is_displayed():
        mobile_navbar.click()
    
    time.sleep(1)
    
    selenium.find_element(By.CSS_SELECTOR, '[data-test="language-select"]').click()
    selenium.find_element(By.CSS_SELECTOR, '[data-test="lang-es"]').click()

    time.sleep(1)
    
    assert "ES" in selenium.find_element(By.CSS_SELECTOR, '[data-test="language-select"]').text
    assert "Ordenar" in selenium.page_source
    assert "Rango de precios" in selenium.page_source
    assert "Buscar" in selenium.page_source
    assert "Por categoría" in selenium.page_source
    assert "Por marca" in selenium.page_source
    assert "Categorías" in selenium.page_source
    assert "Contacto" in selenium.page_source
    assert "Iniciar sesión" in selenium.page_source


def test_switch_language_to_french(selenium):
    selenium.get("https://practicesoftwaretesting.com")
    
    mobile_navbar = selenium.find_element(By.CLASS_NAME, 'navbar-toggler')
    if mobile_navbar.is_displayed():
        mobile_navbar.click()
    
    time.sleep(1)
    
    selenium.find_element(By.CSS_SELECTOR, '[data-test="language-select"]').click()
    selenium.find_element(By.CSS_SELECTOR, '[data-test="lang-fr"]').click()

    time.sleep(1)
    
    assert "FR" in selenium.find_element(By.CSS_SELECTOR, '[data-test="language-select"]').text
    assert "Trier" in selenium.page_source
    assert "Fourchette de prix" in selenium.page_source
    assert "Rechercher" in selenium.page_source
    assert "Par catégorie" in selenium.page_source
    assert "Par marque" in selenium.page_source
    assert "Catégories" in selenium.page_source
    assert "Contact" in selenium.page_source
    assert "Se connecter" in selenium.page_source


def test_switch_language_to_dutch(selenium):
    selenium.get("https://practicesoftwaretesting.com")
    
    mobile_navbar = selenium.find_element(By.CLASS_NAME, 'navbar-toggler')
    if mobile_navbar.is_displayed():
        mobile_navbar.click()
    
    time.sleep(1)
    
    selenium.find_element(By.CSS_SELECTOR, '[data-test="language-select"]').click()
    selenium.find_element(By.CSS_SELECTOR, '[data-test="lang-nl"]').click()

    time.sleep(1)
    
    assert "NL" in selenium.find_element(By.CSS_SELECTOR, '[data-test="language-select"]').text
    assert "Sorteren" in selenium.page_source
    assert "Prijsklasse" in selenium.page_source
    assert "Zoeken" in selenium.page_source
    assert "Op categorie" in selenium.page_source
    assert "Op merk" in selenium.page_source
    assert "Categorieën" in selenium.page_source
    assert "Contact" in selenium.page_source
    assert "Inloggen" in selenium.page_source


def test_switch_language_to_turkish(selenium):
    selenium.get("https://practicesoftwaretesting.com")
    
    mobile_navbar = selenium.find_element(By.CLASS_NAME, 'navbar-toggler')
    if mobile_navbar.is_displayed():
        mobile_navbar.click()
    
    time.sleep(1)
    
    selenium.find_element(By.CSS_SELECTOR, '[data-test="language-select"]').click()
    selenium.find_element(By.CSS_SELECTOR, '[data-test="lang-tr"]').click()

    time.sleep(1)
    
    assert "TR" in selenium.find_element(By.CSS_SELECTOR, '[data-test="language-select"]').text
    assert "Sırala" in selenium.page_source
    assert "Fiyat Aralığı" in selenium.page_source
    assert "Ara" in selenium.page_source
    assert "Kategoriye göre" in selenium.page_source
    assert "Markaya göre" in selenium.page_source
    assert "Kategoriler" in selenium.page_source
    assert "İletişim" in selenium.page_source
    assert "Giriş Yap" in selenium.page_source


def test_search_for_pliers(selenium):
    selenium.get("https://practicesoftwaretesting.com")
    
    time.sleep(2)
    
    mobile_filters = selenium.find_element(By.CSS_SELECTOR, '[data-test="filters"]')
    if mobile_filters.is_displayed():
        mobile_filters.click()
    
    time.sleep(1)
    
    search_input = selenium.find_element(By.CSS_SELECTOR, '[data-test="search-query"]')
    search_input.send_keys("pliers")
    assert search_input.get_attribute("value") == "pliers"

    search_button = selenium.find_element(By.CSS_SELECTOR, '[data-test="search-submit"]')
    assert search_button.is_enabled()
    search_button.click()

    time.sleep(1)

    page = selenium.page_source
    assert "Combination Pliers" in page
    assert "Pliers" in page
    assert "Long Nose Pliers" in page
    assert "Claw Hammer with Shock Reduction Grip" not in page

    first_title = selenium.find_elements(By.CSS_SELECTOR, ".card-title")[0]
    assert "Pliers" in first_title.text


def test_search_nonexistent_product(selenium):
    selenium.get("https://practicesoftwaretesting.com")
    time.sleep(1)
    
    mobile_filters = selenium.find_element(By.CSS_SELECTOR, '[data-test="filters"]')
    if mobile_filters.is_displayed():
        mobile_filters.click()
    
    time.sleep(1)
    
    selenium.find_element(By.CSS_SELECTOR, '[data-test="search-query"]').send_keys("test")
    selenium.find_element(By.CSS_SELECTOR, '[data-test="search-submit"]').click()

    time.sleep(1)
    assert "There are no products found" in selenium.page_source


def test_clear_search_results(selenium):
    selenium.get("https://practicesoftwaretesting.com")
    
    mobile_filters = selenium.find_element(By.CSS_SELECTOR, '[data-test="filters"]')
    if mobile_filters.is_displayed():
        mobile_filters.click()
    
    time.sleep(1)
    
    selenium.find_element(By.CSS_SELECTOR, '[data-test="search-query"]').send_keys("pliers")
    selenium.find_element(By.CSS_SELECTOR, '[data-test="search-submit"]').click()

    time.sleep(1)

    reset_button = selenium.find_element(By.CSS_SELECTOR, '[data-test="search-reset"]')
    assert reset_button.is_displayed()
    reset_button.click()

    time.sleep(1)
    cards = selenium.find_elements(By.CSS_SELECTOR, ".card")
    assert len(cards) > 1


def test_filter_by_hand_saw_category(selenium):
    selenium.get("https://practicesoftwaretesting.com")
    time.sleep(1)
    
    mobile_filters = selenium.find_element(By.CSS_SELECTOR, '[data-test="filters"]')
    if mobile_filters.is_displayed():
        mobile_filters.click()
    
    time.sleep(1)
    
    hand_saw_label = selenium.find_element(By.XPATH, "//label[contains(normalize-space(), 'Hand Saw')]")
    hand_saw_label.click()
    
    checkbox = hand_saw_label.find_element(By.TAG_NAME, "input")
    assert checkbox.is_selected()

    time.sleep(1)

    titles = [el.text for el in selenium.find_elements(By.CSS_SELECTOR, ".card-title")]
    assert any("Wood Saw" in title for title in titles)


def test_filter_by_mightycraft_brand(selenium):
    selenium.get("https://practicesoftwaretesting.com")
    time.sleep(1)
    
    mobile_filters = selenium.find_element(By.CSS_SELECTOR, '[data-test="filters"]')
    if mobile_filters.is_displayed():
        mobile_filters.click()
    
    time.sleep(1)
    
    mightycraft_label = selenium.find_element(By.XPATH, "//label[contains(normalize-space(), 'MightyCraft Hardware')]")
    mightycraft_label.click()
    
    brand_checkbox = mightycraft_label.find_element(By.TAG_NAME, "input")

    assert brand_checkbox.is_selected()

    time.sleep(1)
    
    titles = [el.text for el in selenium.find_elements(By.CSS_SELECTOR, ".card-title")]
    assert any("Claw Hammer" in title for title in titles)


def test_navigate_to_combination_pliers_page(selenium):
    selenium.get("https://practicesoftwaretesting.com")
    time.sleep(1)
    selenium.find_element(By.CSS_SELECTOR, 'a.card:first-of-type').click()

    time.sleep(2)

    name = selenium.find_element(By.CSS_SELECTOR, '[data-test="product-name"]')
    assert "Combination Pliers" in name.text
    assert name.is_displayed()

    description = selenium.find_element(By.CSS_SELECTOR, '[data-test="product-description"]')
    assert description.is_displayed()

    image = selenium.find_element(By.CSS_SELECTOR, 'img[alt="Combination Pliers"]')
    assert image.is_displayed()

    width = selenium.execute_script("return arguments[0].naturalWidth;", image)
    assert width > 0


def test_combination_pliers_price_displayed(selenium): 
    selenium.get("https://practicesoftwaretesting.com")
    time.sleep(2)
    
    name = selenium.find_element(By.CSS_SELECTOR, '[data-test="product-name"]')
    assert "Combination Pliers" in name.text

    price = selenium.find_element(By.CSS_SELECTOR, '[data-test="product-price"]')
    assert price.is_displayed()

    product_card = selenium.find_element(By.XPATH, "//a[contains(@class, 'card') and .//h5[contains(text(), 'Combination Pliers')]]")
    product_price = product_card.find_element(By.CSS_SELECTOR, '[data-test="product-price"]')
    assert "$14.15" in product_price.text


def test_sort_by_name_az(selenium):
    selenium.get("https://practicesoftwaretesting.com")
    time.sleep(1)
    
    mobile_filters = selenium.find_element(By.CSS_SELECTOR, '[data-test="filters"]')
    if mobile_filters.is_displayed():
        mobile_filters.click()
    
    time.sleep(1)
    
    Select(selenium.find_element(By.CSS_SELECTOR, '[data-test="sort"]')).select_by_visible_text("Name (A - Z)")

    time.sleep(2)

    names = [el.text.strip() for el in selenium.find_elements(By.CSS_SELECTOR, ".card-title")]
    assert names == sorted(names)


def test_sort_by_name_za(selenium):
    selenium.get("https://practicesoftwaretesting.com")
    time.sleep(1)
    
    mobile_filters = selenium.find_element(By.CSS_SELECTOR, '[data-test="filters"]')
    if mobile_filters.is_displayed():
        mobile_filters.click()
    
    time.sleep(1)
    
    Select(selenium.find_element(By.CSS_SELECTOR, '[data-test="sort"]')).select_by_visible_text("Name (Z - A)")
    
    time.sleep(3)

    names = [el.text.strip() for el in selenium.find_elements(By.CSS_SELECTOR, ".card-title")]
    assert names == sorted(names, reverse=True)


def test_sort_by_price_low_to_high(selenium):
    selenium.get("https://practicesoftwaretesting.com")
    time.sleep(1)
    
    mobile_filters = selenium.find_element(By.CSS_SELECTOR, '[data-test="filters"]')
    if mobile_filters.is_displayed():
        mobile_filters.click()
    
    time.sleep(1)
    
    Select(selenium.find_element(By.CSS_SELECTOR, '[data-test="sort"]')).select_by_visible_text("Price (Low - High)")

    time.sleep(2)

    prices = [
        float(el.text.replace("$", "").strip())
        for el in selenium.find_elements(By.CSS_SELECTOR, '[data-test="product-price"]')
    ]
    assert prices == sorted(prices)


def test_sort_by_price_high_to_low(selenium):
    selenium.get("https://practicesoftwaretesting.com")
    time.sleep(1)
    
    mobile_filters = selenium.find_element(By.CSS_SELECTOR, '[data-test="filters"]')
    if mobile_filters.is_displayed():
        mobile_filters.click()
    
    time.sleep(1)
    
    Select(selenium.find_element(By.CSS_SELECTOR, '[data-test="sort"]')).select_by_visible_text("Price (High - Low)")

    time.sleep(2)
    
    prices = [
        float(el.text.replace("$", "").strip())
        for el in selenium.find_elements(By.CSS_SELECTOR, '[data-test="product-price"]')
    ]
    assert prices == sorted(prices, reverse=True)