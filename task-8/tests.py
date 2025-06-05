import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

class Tests(unittest.TestCase):
    def setUp(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://practicesoftwaretesting.com")

    def tearDown(cls):
        cls.driver.quit()
        
    def test_open_homepage(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.TAG_NAME, "body"))
        )
        body = self.driver.find_element(By.TAG_NAME, "body")
        self.assertTrue(body.is_displayed())
        
    def test_header_elements(self):
        logo = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[title="Practice Software Testing - Toolshop"]')))
        self.assertTrue(logo.is_displayed())
        self.assertEqual(logo.get_attribute("href"), "https://practicesoftwaretesting.com/")
        
        home_link = self.driver.find_element(By.LINK_TEXT, "Home")
        self.assertTrue(home_link.is_displayed())
        self.assertIn("nav-link", home_link.get_attribute("class"))
        
        categories_link = self.driver.find_element(By.LINK_TEXT, "Categories")
        self.assertTrue(categories_link.is_displayed())
        self.assertIn("nav-link", categories_link.get_attribute("class"))
        
        contacts_link = self.driver.find_element(By.LINK_TEXT, "Contact")
        self.assertTrue(contacts_link.is_displayed())
        self.assertIn("nav-link", contacts_link.get_attribute("class"))
        
        login_link = self.driver.find_element(By.LINK_TEXT, "Sign in")
        self.assertTrue(login_link.is_displayed())
        self.assertIn("nav-link", login_link.get_attribute("class"))
        
    def test_home_link(self):
        home_link = self.driver.find_element(By.LINK_TEXT, "Home")
        self.assertIn("/", home_link.get_attribute("href"))
        
        home_link.click()
        
        time.sleep(1)
        
        home_link = self.driver.find_element(By.LINK_TEXT, "Home")
        self.assertIn("nav-link active", home_link.get_attribute("class"))
        
    def test_contacts_link(self):
        contacts_link = self.driver.find_element(By.LINK_TEXT, "Contact")
        self.assertIn("/contact", contacts_link.get_attribute("href"))
        
        contacts_link.click()
        time.sleep(1)
        
        element = self.driver.find_element(By.XPATH, "//h3[text()='Contact']")
        self.assertTrue(element.is_displayed())
        
    def test_login_link(self):
        login_link = self.driver.find_element(By.LINK_TEXT, "Sign in")
        self.assertIn("/auth/login", login_link.get_attribute("href"))
        
        login_link.click()
                
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h3[text()='Login']")))
        self.assertTrue(element.is_displayed())
        
    def test_register_link(self):
        self.driver.find_element(By.LINK_TEXT, "Sign in").click()
        
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="register-link"]').click()
                
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h3[text()='Customer registration']")))
        self.assertTrue(element.is_displayed())
        
    def test_forgot_password_link(self):
        self.driver.find_element(By.LINK_TEXT, "Sign in").click()
        
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="forgot-password-link"]').click()
                
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h3[text()='Forgot Password']")))
        self.assertTrue(element.is_displayed())
    
    def test_categories_dropdown(self):
        categories_button = self.driver.find_element(By.CSS_SELECTOR, '[data-test="nav-categories"]')
        categories_button.click()
        
        dropdown = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".navbar-nav > .dropdown > .dropdown-menu")))
        self.assertTrue(dropdown.is_displayed())
        
        hand_tools_link = self.driver.find_element(By.CSS_SELECTOR, '[data-test="nav-hand-tools"]')
        self.assertIn("Hand Tools", hand_tools_link.text)
        
    def test_hand_tools_link(self):
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="nav-categories"]').click()
        
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="nav-hand-tools"]').click()
        time.sleep(1)
        
        element = self.driver.find_element(By.XPATH, "//h2[text()='Category: Hand Tools']")
        self.assertTrue(element.is_displayed())
        
    def test_power_tools_link(self):
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="nav-categories"]').click()
        
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="nav-power-tools"]').click()
        time.sleep(1)
        
        element = self.driver.find_element(By.XPATH, "//h2[text()='Category: Power Tools']")
        self.assertTrue(element.is_displayed())
        
    def test_other_link(self):
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="nav-categories"]').click()

        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="nav-other"]').click()
        time.sleep(1)
        
        element = self.driver.find_element(By.XPATH, "//h2[text()='Category: Other']")
        self.assertTrue(element.is_displayed())
        
    def test_special_tools_link(self):
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="nav-categories"]').click()
        
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="nav-special-tools"]').click()
        time.sleep(1)
        
        element = self.driver.find_element(By.XPATH, "//h2[text()='Category: Special Tools']")
        self.assertTrue(element.is_displayed())
    
    def test_rentals_link(self):
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="nav-categories"]').click()
        
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="nav-rentals"]').click()
        time.sleep(1)
        
        element = self.driver.find_element(By.XPATH, "//h1[text()='Rentals']")
        self.assertTrue(element.is_displayed())
        
    def test_switch_language_to_german(self):
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="language-select"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="lang-de"]').click()

        time.sleep(1)
        
        self.assertIn("DE", self.driver.find_element(By.CSS_SELECTOR, '[data-test="language-select"]').text)
        self.assertIn("Sortieren", self.driver.page_source)
        self.assertIn("Preisspanne", self.driver.page_source)
        self.assertIn("Suche", self.driver.page_source)
        self.assertIn("Nach Kategorie", self.driver.page_source)
        self.assertIn("Nach Marken", self.driver.page_source)
        self.assertIn("Kategorien", self.driver.page_source)
        self.assertIn("Kontakt", self.driver.page_source)
        self.assertIn("Einloggen", self.driver.page_source)
        
    def test_switch_language_to_english(self):
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="language-select"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="lang-en"]').click()

        time.sleep(1)
        
        self.assertIn("EN", self.driver.find_element(By.CSS_SELECTOR, '[data-test="language-select"]').text)
        self.assertIn("Sort", self.driver.page_source)
        self.assertIn("Price Range", self.driver.page_source)
        self.assertIn("Search", self.driver.page_source)
        self.assertIn("By category", self.driver.page_source)
        self.assertIn("By brand", self.driver.page_source)
        self.assertIn("Categories", self.driver.page_source)
        self.assertIn("Contact", self.driver.page_source)
        self.assertIn("Sign in", self.driver.page_source)
        
    def test_switch_language_to_spanish(self):
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="language-select"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="lang-es"]').click()

        time.sleep(1)
        
        self.assertIn("ES", self.driver.find_element(By.CSS_SELECTOR, '[data-test="language-select"]').text)
        self.assertIn("Ordenar", self.driver.page_source)
        self.assertIn("Rango de precios", self.driver.page_source)
        self.assertIn("Buscar", self.driver.page_source)
        self.assertIn("Por categoría", self.driver.page_source)
        self.assertIn("Por marca", self.driver.page_source)
        self.assertIn("Categorías", self.driver.page_source)
        self.assertIn("Contacto", self.driver.page_source)
        self.assertIn("Iniciar sesión", self.driver.page_source)
        
    def test_switch_language_to_french(self):
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="language-select"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="lang-fr"]').click()

        time.sleep(1)
        
        self.assertIn("FR", self.driver.find_element(By.CSS_SELECTOR, '[data-test="language-select"]').text)
        self.assertIn("Trier", self.driver.page_source)
        self.assertIn("Fourchette de prix", self.driver.page_source)
        self.assertIn("Rechercher", self.driver.page_source)
        self.assertIn("Par catégorie", self.driver.page_source)
        self.assertIn("Par marque", self.driver.page_source)
        self.assertIn("Catégories", self.driver.page_source)
        self.assertIn("Contact", self.driver.page_source)
        self.assertIn("Se connecter", self.driver.page_source)
        
    def test_switch_language_to_dutch(self):
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="language-select"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="lang-nl"]').click()

        time.sleep(1)
        
        self.assertIn("NL", self.driver.find_element(By.CSS_SELECTOR, '[data-test="language-select"]').text)
        self.assertIn("Sorteren", self.driver.page_source)
        self.assertIn("Prijsklasse", self.driver.page_source)
        self.assertIn("Zoeken", self.driver.page_source)
        self.assertIn("Op categorie", self.driver.page_source)
        self.assertIn("Op merk", self.driver.page_source)
        self.assertIn("Categorieën", self.driver.page_source)
        self.assertIn("Contact", self.driver.page_source)
        self.assertIn("Inloggen", self.driver.page_source)
    
        
    def test_switch_language_to_turkish(self):
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="language-select"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="lang-tr"]').click()

        time.sleep(1)
        
        self.assertIn("TR", self.driver.find_element(By.CSS_SELECTOR, '[data-test="language-select"]').text)
        self.assertIn("Sırala", self.driver.page_source)
        self.assertIn("Fiyat Aralığı", self.driver.page_source)
        self.assertIn("Ara", self.driver.page_source)
        self.assertIn("Kategoriye göre", self.driver.page_source)
        self.assertIn("Markaya göre", self.driver.page_source)
        self.assertIn("Kategoriler", self.driver.page_source)
        self.assertIn("İletişim", self.driver.page_source)
        self.assertIn("Giriş Yap", self.driver.page_source)
        
    def test_search_for_pliers(self):
        search_input = self.driver.find_element(By.CSS_SELECTOR, '[data-test="search-query"]')
        search_input.send_keys("pliers")
        self.assertEqual(search_input.get_attribute("value"), "pliers")

        search_button = self.driver.find_element(By.CSS_SELECTOR, '[data-test="search-submit"]')
        self.assertTrue(search_button.is_enabled())
        search_button.click()

        time.sleep(1)

        page = self.driver.page_source
        self.assertIn("Combination Pliers", page)
        self.assertIn("Pliers", page)
        self.assertIn("Long Nose Pliers", page)
        self.assertNotIn("Claw Hammer with Shock Reduction Grip", page)

        first_title = self.driver.find_elements(By.CSS_SELECTOR, ".card-title")[0]
        self.assertIn("Pliers", first_title.text)
        
    def test_search_nonexistent_product(self):
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="search-query"]').send_keys("test")
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="search-submit"]').click()

        time.sleep(1)
        self.assertIn("There are no products found", self.driver.page_source)
    
    def test_clear_search_results(self):
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="search-query"]').send_keys("pliers")
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="search-submit"]').click()

        time.sleep(1)

        reset_button = self.driver.find_element(By.CSS_SELECTOR, '[data-test="search-reset"]')
        self.assertTrue(reset_button.is_displayed())
        reset_button.click()

        time.sleep(1)
        cards = self.driver.find_elements(By.CSS_SELECTOR, ".card")
        self.assertGreater(len(cards), 1)
    
    def test_filter_by_hand_saw_category(self):
        time.sleep(1)
        
        hand_saw_label = self.driver.find_element(By.XPATH, "//label[contains(normalize-space(), 'Hand Saw')]")
        hand_saw_label.click()
        
        checkbox = hand_saw_label.find_element(By.TAG_NAME, "input")
        self.assertTrue(checkbox.is_selected())

        time.sleep(1)

        titles = [el.text for el in self.driver.find_elements(By.CSS_SELECTOR, ".card-title")]
        self.assertTrue(any("Wood Saw" in title for title in titles))
        
    def test_filter_by_mightycraft_brand(self):
        time.sleep(1)
        
        mightycraft_label = self.driver.find_element(By.XPATH, "//label[contains(normalize-space(), 'MightyCraft Hardware')]")
        mightycraft_label.click()
        
        brand_checkbox = mightycraft_label.find_element(By.TAG_NAME, "input")

        self.assertTrue(brand_checkbox.is_selected())

        time.sleep(1)
        
        titles = [el.text for el in self.driver.find_elements(By.CSS_SELECTOR, ".card-title")]
        self.assertTrue(any("Claw Hammer" in title for title in titles))
        
    def test_navigate_to_combination_pliers_page(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//a[contains(@class, 'card') and .//h5[contains(text(), 'Combination Pliers')]]").click()

        time.sleep(1)

        name = self.driver.find_element(By.CSS_SELECTOR, '[data-test="product-name"]')
        self.assertIn("Combination Pliers", name.text)
        self.assertTrue(name.is_displayed())

        description = self.driver.find_element(By.CSS_SELECTOR, '[data-test="product-description"]')
        self.assertTrue(description.is_displayed())

        image = self.driver.find_element(By.CSS_SELECTOR, 'img[alt="Combination Pliers"]')
        self.assertTrue(image.is_displayed())

        width = self.driver.execute_script("return arguments[0].naturalWidth;", image)
        self.assertGreater(width, 0)        
    
    def test_combination_pliers_price_displayed(self): 
        time.sleep(1)
        
        name = self.driver.find_element(By.CSS_SELECTOR, '[data-test="product-name"]')
        self.assertIn("Combination Pliers", name.text)

        price = self.driver.find_element(By.CSS_SELECTOR, '[data-test="product-price"]')
        self.assertTrue(price.is_displayed())

        product_card = self.driver.find_element(By.XPATH, "//a[contains(@class, 'card') and .//h5[contains(text(), 'Combination Pliers')]]")
        product_price = product_card.find_element(By.CSS_SELECTOR, '[data-test="product-price"]')
        self.assertIn("$14.15", product_price.text)
    
    def test_sort_by_name_az(self):
        Select(self.driver.find_element(By.CSS_SELECTOR, '[data-test="sort"]')).select_by_visible_text("Name (A - Z)")

        time.sleep(1)

        names = [el.text.strip() for el in self.driver.find_elements(By.CSS_SELECTOR, ".card-title")]
        self.assertEqual(names, sorted(names))
        
    def test_sort_by_name_za(self):
        Select(self.driver.find_element(By.CSS_SELECTOR, '[data-test="sort"]')).select_by_visible_text("Name (Z - A)")
        
        time.sleep(1)

        names = [el.text.strip() for el in self.driver.find_elements(By.CSS_SELECTOR, ".card-title")]
        self.assertEqual(names, sorted(names, reverse=True))
    
    def test_sort_by_price_low_to_high(self):
        Select(self.driver.find_element(By.CSS_SELECTOR, '[data-test="sort"]')).select_by_visible_text("Price (Low - High)")

        time.sleep(1)

        prices = [
            float(el.text.replace("$", "").strip())
            for el in self.driver.find_elements(By.CSS_SELECTOR, '[data-test="product-price"]')
        ]
        self.assertEqual(prices, sorted(prices))
    
    def test_sort_by_price_high_to_low(self):
        Select(self.driver.find_element(By.CSS_SELECTOR, '[data-test="sort"]')).select_by_visible_text("Price (High - Low)")

        time.sleep(1)
        
        prices = [
            float(el.text.replace("$", "").strip())
            for el in self.driver.find_elements(By.CSS_SELECTOR, '[data-test="product-price"]')
        ]
        self.assertEqual(prices, sorted(prices, reverse=True))
        
if __name__ == "__main__":
    unittest.main()