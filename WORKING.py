from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

with open("long_description.txt", "r") as file:
    long_description = file.read()

with open("technical_information.txt", "r") as file:
    technical_information = file.read()

with open("cushions_long_description.txt", "r") as file:
    cushions_long_description = file.read()

with open("cushions_technical_information.txt", "r") as file:
    cushions_technical_information = file.read()

with open("Romans_long_description.txt", "r") as file:
    romans_long_description = file.read()

with open("Romans_technical_information.txt", "r") as file:
    romans_technical_information = file.read()

with open("Fabric_long_description.txt", "r") as file:
    fabric_long_description = file.read()

with open("Fabric_technical_information.txt", "r") as file:
    fabric_technical_information = file.read()

# Define the new variable declarations
#product_name = "the best blind in the world"
#long_description = "HJVHJBH"
#technical_information = "Technical Information"
fabric_composition = "100% POLYESTER"
cleaning_instructions = "Wipe Clean"
blind_collection = "Quinton Blackout"
brand_name = "Louvolite"
#color_choice = "Pink"
fabric_design_types = "PLAIN TEXTURED"
#uv_light_options = "Standard"
product_range = "Quinton Blackout vertical "
blind_types = ["Vertical Blind"]
product_types = ["Vertical Blind", "Replacement Vertical Slats"]
product_categories = [
    "Made To Measure Blinds",
    "Made To Measure Curtains",
    "Roman Blinds",
    "Curtain Fabric",
    "Accessories",
    "Cushions",
    "By Colour",
    "Pink"
]
product_price = "25"
price_band_option = "4.89mm Vertical - Price Band B"
#replacement_slats_long_description = "89mm Louvres Only"
#replacement_slats_technical_description = "Technical Information"
max_drop_value = "300"
max_width_rotated_value = "300"
replacement_slats_price_band = "Price Band Example"
fabric_width = "400"
pattern_repeat = "30cm"
# Your original code follows here...
# ...


# Your original code follows here...
# ...




from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def upload_product_to_site(driver, product_name, colors):

        driver = webdriver.Chrome()

        # Navigate to the login page
        # Update with the actual URL
        driver.get("https://www.emeraldblindsandcurtains.co.uk/z-admin/login/")

        # Locate the username and password input fields by their class names
        username_field = driver.find_element(
                By.CLASS_NAME, "form-control[name='email']")
        password_field = driver.find_element(
                By.CLASS_NAME, "form-control[name='password']")

        # Input your credentials and submit the form
        username_field.send_keys("shaun_mcgrath451@btinternet.com")
        password_field.send_keys("zBURS0MzzJ@gwTyiLzGIHgObkChm")
        password_field.send_keys(Keys.RETURN)  # Simulate pressing the Enter key

        accept_button = driver.find_element(By.LINK_TEXT, "Accept")
        accept_button.click()

        dashboard_button = driver.find_element(
                By.XPATH, "//a[contains(@href, '/z-admin/') and contains(@class, 'btn-primary') and contains(text(), 'Dashboard')]")
        dashboard_button.click()

        driver.maximize_window()
        # You might need to add a delay here to allow the page to process the login
        time.sleep(2)

        new_window_handle = driver.window_handles[-1]
        driver.switch_to.window(new_window_handle)

        # # new_url = "https://www.emeraldblindsandcurtains.co.uk/z-admin/products/view/4955/"
        # # driver.get(new_url)
        # new_url = "https://www.emeraldblindsandcurtains.co.uk/z-admin/products/create/"
        # driver.get(new_url)

        # ... (your existing code)

        # Product details
        product_name = product_name
        attribute_set = "Default"
        product_type = "Simple"

        # Navigate to the "Create New Product" page
        new_url = "https://www.emeraldblindsandcurtains.co.uk/z-admin/products/create/"
        driver.get(new_url)
        time.sleep(2)


        # Fill in the product details
        title_field = driver.find_element(By.NAME, "sku")  # SKU field
        attribute_dropdown = driver.find_element(By.NAME, "attribute_group_id")
        product_type_dropdown = driver.find_element(By.NAME, "product_type_id")

        title_field.send_keys(product_name)

        # Select the attribute set from the dropdown
        attribute_option = attribute_dropdown.find_element(
                By.XPATH, f"//option[text()='{attribute_set}']")
        attribute_option.click()

        # Select the product type from the dropdown
        product_type_option = product_type_dropdown.find_element(
                By.XPATH, f"//option[text()='{product_type}']")
        product_type_option.click()

        # Locate and click the "Save" button
        save_button = driver.find_element(
                By.XPATH, "//button[contains(text(), 'Save')]")
        save_button.click()

        time.sleep(3)


        # Fill in the title input field
        # Scroll to the title section
        title_section = driver.find_element(
                By.XPATH, "//h4[contains(@class, 'panel-title') and contains(text(), 'Product Information')]")
        driver.execute_script("arguments[0].scrollIntoView();", title_section)
        time.sleep(2)  # Wait for the page to scroll

        # Locate and interact with the title input field
        title_input = driver.find_element(By.NAME, "attribute-id-1")
        title_input.send_keys(product_name)

        # Wait for the dropdown to be clickable
        dropdown = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                        (By.CSS_SELECTOR, "span.select2-selection__rendered[title='Please Select']"))
        )

        # Click the dropdown to open it
        dropdown.click()

        # Locate the option by value and click it
        option = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//li[text()='Catalog, Search']"))
        )
        option.click()


        # Scroll down to the "Long Description" section
        long_description_section = driver.find_element(
                By.XPATH, "//strong[contains(text(), 'Long Description')]")
        driver.execute_script(
                "arguments[0].scrollIntoView();", long_description_section)

        # Locate the iframe element
        iframe = driver.find_element(
                By.XPATH, "//iframe[@title='Rich Text Editor, attribute-id-41']")

        # Switch focus to the iframe
        driver.switch_to.frame(iframe)

        # Now you can interact with the content within the iframe
        # For example, clear the content and enter your own
        text_area = driver.find_element(
                By.XPATH, "//body[@class='cke_editable cke_editable_themed cke_contents_ltr cke_show_borders']")
        text_area.clear()
        text_area.send_keys(long_description)

        # Switch back to the main content
        driver.switch_to.default_content()

        # Locate the iframe element for the technical information
        iframe = driver.find_element(
                By.XPATH, "//iframe[@title='Rich Text Editor, attribute-id-85']")

        # Switch focus to the iframe
        driver.switch_to.frame(iframe)

        # Now you can interact with the content within the iframe
        # For example, clear the content and enter your own
        text_area = driver.find_element(
                By.XPATH, "//body[@class='cke_editable cke_editable_themed cke_contents_ltr cke_show_borders']")
        text_area.clear()
        text_area.send_keys(technical_information)

        # Switch back to the main content
        driver.switch_to.default_content()

        # Scroll down to the "Fabric Width" section
        fabric_width_section = driver.find_element(
                By.XPATH, "//strong[contains(text(), 'Fabric Width')]")
        driver.execute_script("arguments[0].scrollIntoView();", fabric_width_section)

        # Enter the value into the input field for fabric width
        fabric_width_input = driver.find_element(By.NAME, "attribute-id-36")
        fabric_width_input.send_keys(fabric_width)

        # Scroll down to the "Fabric Composition" section
        fabric_composition_section = driver.find_element(
                By.XPATH, "//strong[contains(text(), 'Fabric Composition')]")
        driver.execute_script(
                "arguments[0].scrollIntoView();", fabric_composition_section)

        # Enter "100% POLYESTER" into the input field for fabric composition
        fabric_composition_input = driver.find_element(
                By.NAME, "attribute-id-37")  # Assuming attribute ID is 37
        fabric_composition_input.send_keys(fabric_composition)

        # Scroll down to the "Cleaning Instructions" section
        cleaning_instructions_section = driver.find_element(
                By.XPATH, "//strong[contains(text(), 'Cleaning Instructions')]")
        driver.execute_script(
                "arguments[0].scrollIntoView();", cleaning_instructions_section)

        # Enter "Wipe Clean" into the input field for cleaning instructions
        cleaning_instructions_input = driver.find_element(
                By.NAME, "attribute-id-38")  # Assuming attribute ID is 38
        cleaning_instructions_input.send_keys(cleaning_instructions)

        # Scroll down to the "Collection" section
        collection_section = driver.find_element(
                By.XPATH, "//strong[contains(text(), 'Collection')]")
        driver.execute_script("arguments[0].scrollIntoView();", collection_section)

        # Enter "Palette Vertical" into the input field for collection
        collection_input = driver.find_element(
                By.NAME, "attribute-id-39")  # Assuming attribute ID is 39
        collection_input.send_keys(blind_collection)

        # Scroll down to the "Brand" section
        brand_section = driver.find_element(
                By.XPATH, "//strong[contains(text(), 'Brand')]")
        driver.execute_script("arguments[0].scrollIntoView();", brand_section)

        # Enter "Eclipse" into the input field for brand
        brand_input = driver.find_element(
                By.NAME, "attribute-id-40")  # Assuming attribute ID is 40
        brand_input.send_keys(brand_name)

        time.sleep(1)

        # Scroll down to the color section
        color_section = driver.find_element(
                By.XPATH, "//strong[contains(text(), 'Colour')]")
        driver.execute_script("arguments[0].scrollIntoView();", color_section)

        # Locate the input field of the color dropdown
        color_input = driver.find_element(
                By.CSS_SELECTOR, "input.select2-search__field")

        for color in colors:
                color_input.send_keys(color)
                color_input.send_keys(Keys.RETURN)


        # Scroll down to the "Design Types" section
        design_types_section = driver.find_element(
                By.XPATH, "//strong[contains(text(), 'Design Types')]")
        driver.execute_script("arguments[0].scrollIntoView();", design_types_section)

        # Find the input field for "Design Types" and enter "PLAIN"
        design_types_input = driver.find_element(
                By.NAME, "attribute-id-66")  # Assuming attribute ID is 66
        design_types_input.send_keys(fabric_design_types)

        time.sleep(1)

        #UV LIGHT OPTIONS
        # Wait for the dropdown to be clickable
        dropdown_locator = (By.XPATH, '//*[@id="tabGeneral"]/div[30]/div[2]/div/div/span/span[1]/span/span[2]')
        dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(dropdown_locator))

        # Click the dropdown to open it
        dropdown.click()

        # Locate and click the "Standard" option
        option_locator = (By.XPATH, '//li[text()="Blackout"]')
        option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(option_locator))
        option.click()

        #CURTAIN PATTERN REPEAT
        # Scroll down to the "Pattern Repeat" section
        pattern_repeat_section = driver.find_element(
                By.XPATH, "//strong[contains(text(), 'Pattern Repeat')]")
        driver.execute_script("arguments[0].scrollIntoView();", pattern_repeat_section)

        # Find the input field for "Pattern Repeat" and enter "repeat value"
        pattern_repeat_input = driver.find_element(
                By.NAME, "attribute-id-20")  # Assuming attribute ID is 20
        pattern_repeat_input.send_keys(pattern_repeat)

        #SELECT CURTAIN SETUP
        
        # Wait for the dropdown to be clickable
        curtain_setup_dropdown_locator = (By.XPATH, '//*[@id="tabGeneral"]/div[46]/div[2]/div/div/span/span[1]/span/ul')
        dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(curtain_setup_dropdown_locator))

        # Click the dropdown to open it
        dropdown.click()

        # Locate and click the "Standard" option
        curtain_setup_option_locator = (By.XPATH, '//li[text()="Standard"]')
        option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(curtain_setup_option_locator))
        option.click()


        # Scroll down to the "Product Range" input box
        product_range_section = driver.find_element(
                By.XPATH, "//strong[contains(text(), 'Product Range')]")
        driver.execute_script("arguments[0].scrollIntoView();", product_range_section)

        # Enter "Palette Vertical" in the input box
        product_range_input = driver.find_element(
                By.NAME, "attribute-id-86")  # Adjust the attribute ID if needed
        product_range_input.send_keys(product_range)

        # Scroll down to the "Blind - Types" dropdown
        blind_types_section = driver.find_element(
                By.XPATH, "//strong[contains(text(), 'Blind - Types')]")
        driver.execute_script("arguments[0].scrollIntoView();", blind_types_section)

        # Execute JavaScript to select "Roman Blind" option
        script = """
        var selectElement = document.querySelector('select[name="attribute-id-43[]"]');
        var optionElement = selectElement.querySelector('option[value="Roman Blind"]');
        optionElement.selected = true;
        selectElement.dispatchEvent(new Event('change', { bubbles: true }));
        """
        driver.execute_script(script)


        time.sleep(2)


        # Execute JavaScript to select all values  Roman blinds, curtains, cushions, fabric
        script = """
        var selectElement = document.querySelector('select[name="attribute-id-162[]"]');
        var optionElement1 = selectElement.querySelector('option[value="Roman Blind"]');
        var optionElement2 = selectElement.querySelector('option[value="Cushion"]');
        var optionElement3 = selectElement.querySelector('option[value="Curtain"]');
        var optionElement4 = selectElement.querySelector('option[value="Fabric"]');
        optionElement1.selected = true;
        optionElement2.selected = true;
        optionElement3.selected = true;
        optionElement4.selected = true;
        selectElement.dispatchEvent(new Event('change', { bubbles: true }));
        """
        driver.execute_script(script)

        time.sleep(1)

        



        # Scroll down to the "Product Categories" section
        category_section = driver.find_element(
                By.XPATH, "//h4[contains(text(), 'Product Categories')]")
        driver.execute_script("arguments[0].scrollIntoView();", category_section)
        time.sleep(2)  # Wait for the page to scroll

        # Find the checkbox elements for the specified categories
        categories_to_check = product_categories

        for category in categories_to_check:
                checkbox_xpath = f"//label[contains(text(), '{category}')]/input"
                checkbox = driver.find_element(By.XPATH, checkbox_xpath)

                if not checkbox.is_selected():
                        checkbox.click()

        # Scroll to the top of the page
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)  # Wait for the page to scroll

        # Click the "Save" button
        save_button = driver.find_element(
                By.XPATH, "//button[contains(text(), 'Save')]")
        save_button.click()







        # #############################################PAGE 2#############################################

        # new_url = "https://www.emeraldblindsandcurtains.co.uk/z-admin/products/view/5001/"
        # driver.get(new_url)
        # time.sleep(5)

        # Find the element using a CSS selector with the data-tab attribute
        # Find the element using a complex XPath expression
        element = driver.find_element(By.XPATH, '//a[@class="tab-link"]/strong[text()="Pricing"]')

        # Interact with the element (e.g., click)
        element.click()



        # Locate the input field
        input_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, 'attribute-id-5'))
        )

        # Clear the existing value and input "25"
        input_field.clear()
        input_field.send_keys(product_price)

        #taxable goods

        # Find and click on the main element
        main_element = driver.find_element(By.XPATH, '//*[@id="tabPricing"]/div[5]/div[2]/div/div/span/span[1]/span/span[2]')
        main_element.click()

        # Wait for the dropdown to appear
        wait = WebDriverWait(driver, 10)
        dropdown_option = wait.until(EC.presence_of_element_located((By.XPATH, '//li[text()="Taxable Goods"]')))

        # Click on the "Taxable Goods" option
        dropdown_option.click()

        # Scroll to the top of the page
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)  # Wait for the page to scroll

        # Click the "Save" button
        save_button = driver.find_element(
                By.XPATH, "//button[contains(text(), 'Save')]")
        save_button.click()

        time.sleep(4)
        #CLICK PRICING TABLE AGAIN
        element = driver.find_element(By.XPATH, '//a[@class="tab-link"]/strong[text()="Pricing"]')

        # Interact with the element (e.g., click)
        element.click()

        #SET CUSTOM PRICING MATRIX FOR ROMAN BLIND
        wait = WebDriverWait(driver, 10)
        link_element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tabPricing"]/div[7]/div[2]/a')))

        driver.execute_script("arguments[0].click();", link_element)

        time.sleep(1)

        #Wait for the dropdown to be clickable
        roman_band_selector = (By.XPATH, '/html/body/section/div[2]/div/div[2]/form/div[2]/div[2]/div[5]/div[1]/div/span/span[1]/span/span[2]')
        dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(roman_band_selector))

        # Click the dropdown to open it
        dropdown.click()

        # Locate and click the "Standard" option
        option_locator = (By.XPATH, '//li[text()="Romans Blinds - Price Band B"]')
        option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(option_locator))
        option.click()


        # Scroll to the top of the page
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)  # Wait for the page to scroll

        # Click the "Save Changes" button
        save_changes = driver.find_element(By.XPATH, "//input[contains(@value, 'Save Changes')]")
        save_changes.click()


        #GO BACK 2 PAGES
        driver.back()
        driver.back()

        #CLICK PRODUCT TYPE SPECIFICS TAB
        product_type_tab = driver.find_element(By.XPATH, '//a[@class="tab-link"]/strong[text()="Product Type Specifics"]')

        # Interact with the element (e.g., click)
        product_type_tab.click()

        #SELECT REPLACEMENT VERTICAL SLATS FROM THE PRODUCT TYPE SPECIFICS TAB

        # Find the dropdown element
        dropdown = Select(driver.find_element(By.CSS_SELECTOR, ".form-control.select2-hidden-accessible[data-role='product-type-specifics-select']"))

        # Select the option by its visible text
        dropdown.select_by_visible_text('Roman Blind')


        #REPLACEMENT SLATS LONG DESCRIPTION
        # Scroll down to the section containing the iframe (assuming its characteristic is similar to the previous "Long Description" section, but if it's different, adjust the XPath accordingly)
        section = driver.find_element(
                By.XPATH, "//div[@id='cke_14_contents']")
        driver.execute_script(
                "arguments[0].scrollIntoView();", section)

        # Locate the new iframe element using its title
        iframe = driver.find_element(
                By.XPATH, "//iframe[@title='Rich Text Editor, product-type-specifics[roman blind][41]")

        # Switch focus to the iframe
        driver.switch_to.frame(iframe)

        # Assuming that the structure inside the iframe is similar to before
        text_area = driver.find_element(
                By.XPATH, "//body[@class='cke_editable cke_editable_themed cke_contents_ltr cke_show_borders']")
        text_area.clear()
        text_area.send_keys(romans_long_description)

        # Switch back to the main content
        driver.switch_to.default_content()

        #TECHNICAL INFO FOR REPLACEMENT SLATS
        # Locate the new iframe element for the "technical information box" using its title
        iframe_technical = driver.find_element(
                By.XPATH, "//iframe[@title='Rich Text Editor, product-type-specifics[roman blind][85]']")

        # Switch focus to the iframe
        driver.switch_to.frame(iframe_technical)

        # Assuming that the structure inside the iframe is similar to the previous one
        text_area_technical = driver.find_element(
                By.XPATH, "//body[@class='cke_editable cke_editable_themed cke_contents_ltr cke_show_borders']")
        text_area_technical.clear()
        text_area_technical.send_keys(romans_technical_information)

        # Switch back to the main content
        driver.switch_to.default_content()


        # #REPLACEMENT SLATS MAX DROP
        # # Scroll down to the section containing the input
        # div_element = driver.find_element(
        #         By.XPATH, "//div[@class='col-md-10 col-lg-9']")
        # driver.execute_script(
        #         "arguments[0].scrollIntoView();", div_element)

        # # Locate the input box and send the value "300"
        # input_box = driver.find_element(
        #         By.XPATH, "//div[@class='col-md-10 col-lg-9']//input[@name='product-type-specifics[replacement vertical slats][164]']")
        # input_box.clear()  # Clear existing value if any
        # input_box.send_keys(max_drop_value)

        # # MAX WIDTH ROTATED
        # # Locate the input box and send the value "300"
        # input_box = driver.find_element(
        #         By.XPATH, "//div[@class='col-md-10 col-lg-9']//input[@name='product-type-specifics[replacement vertical slats][91]']")
        # input_box.clear()  # Clear existing value if any
        # input_box.send_keys(max_width_rotated_value)

        # #REPLACEMENT SLATA FABRIC WIDTH
        # # Locate the input box and send the value "300"
        # input_box = driver.find_element(
        #         By.XPATH, "//div[@class='col-md-10 col-lg-9']//input[@name='product-type-specifics[replacement vertical slats][36]']")
        # input_box.clear()  # Clear existing value if any
        # input_box.send_keys("300")

        #SCROLL TO TOP OF THE PAGHE AND PRESS SAVE
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)  # Wait for the page to scroll

        # Click the "Save" button
        save_button = driver.find_element(
                By.XPATH, "//button[contains(text(), 'Save')]")
        save_button.click()

        #CLICK PRODUCT TYPE SPECIFICS TAB
        product_type_tab = driver.find_element(By.XPATH, '//a[@class="tab-link"]/strong[text()="Product Type Specifics"]')

        # Interact with the element (e.g., click)
        product_type_tab.click()

        #SELECT REPLACEMENT CUSHIONS FROM THE PRODUCT TYPE SPECIFICS TAB

        # Find the dropdown element
        dropdown = Select(driver.find_element(By.CSS_SELECTOR, ".form-control.select2-hidden-accessible[data-role='product-type-specifics-select']"))

        # Select the option by its visible text
        dropdown.select_by_visible_text('Cushion')

        #REPLACEMENT SLATS LONG DESCRIPTION
        # Scroll down to the section containing the iframe (assuming its characteristic is similar to the previous "Long Description" section, but if it's different, adjust the XPath accordingly)
        section = driver.find_element(
                By.XPATH, "//div[@id='cke_17_contents']")
        driver.execute_script(
                "arguments[0].scrollIntoView();", section)

        # Locate the new iframe element using its title
        iframe = driver.find_element(
                By.XPATH, "//iframe[@title='Rich Text Editor, product-type-specifics[cushion][41]")

        # Switch focus to the iframe
        driver.switch_to.frame(iframe)

        # Assuming that the structure inside the iframe is similar to before
        text_area = driver.find_element(
                By.XPATH, "//body[@class='cke_editable cke_editable_themed cke_contents_ltr cke_show_borders']")
        text_area.clear()
        text_area.send_keys(cushions_long_description)

        # Switch back to the main content
        driver.switch_to.default_content()

        #TECHNICAL INFO FOR REPLACEMENT SLATS
        # Locate the new iframe element for the "technical information box" using its title
        iframe_technical = driver.find_element(
                By.XPATH, "//iframe[@title='Rich Text Editor, product-type-specifics[cushion][85]']")

        # Switch focus to the iframe
        driver.switch_to.frame(iframe_technical)

        # Assuming that the structure inside the iframe is similar to the previous one
        text_area_technical = driver.find_element(
                By.XPATH, "//body[@class='cke_editable cke_editable_themed cke_contents_ltr cke_show_borders']")
        text_area_technical.clear()
        text_area_technical.send_keys(cushions_technical_information)

        # Switch back to the main content
        driver.switch_to.default_content()

        #SCROLL TO TOP OF THE PAGHE AND PRESS SAVE
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)  # Wait for the page to scroll

        # Click the "Save" button
        save_button = driver.find_element(
                By.XPATH, "//button[contains(text(), 'Save')]")
        save_button.click()

        #SELECT FABRIC FROM THE PRODUCT TYPE SPECIFICS TAB

        # Find the dropdown element
        dropdown = Select(driver.find_element(By.CSS_SELECTOR, ".form-control.select2-hidden-accessible[data-role='product-type-specifics-select']"))

        # Select the option by its visible text
        dropdown.select_by_visible_text('Fabric')

        #REPLACEMENT SLATS LONG DESCRIPTION
        # Scroll down to the section containing the iframe (assuming its characteristic is similar to the previous "Long Description" section, but if it's different, adjust the XPath accordingly)
        section = driver.find_element(
                By.XPATH, "//div[@id='cke_23_contents']")
        driver.execute_script(
                "arguments[0].scrollIntoView();", section)

        # Locate the new iframe element using its title
        iframe = driver.find_element(
                By.XPATH, "//iframe[@title='Rich Text Editor, product-type-specifics[fabric][41]")

        # Switch focus to the iframe
        driver.switch_to.frame(iframe)

        # Assuming that the structure inside the iframe is similar to before
        text_area = driver.find_element(
                By.XPATH, "//body[@class='cke_editable cke_editable_themed cke_contents_ltr cke_show_borders']")
        text_area.clear()
        text_area.send_keys(fabric_long_description)

        # Switch back to the main content
        driver.switch_to.default_content()

        #TECHNICAL INFO FOR REPLACEMENT SLATS
        # Locate the new iframe element for the "technical information box" using its title
        iframe_technical = driver.find_element(
                By.XPATH, "//iframe[@title='Rich Text Editor, product-type-specifics[fabric][85]']")

        # Switch focus to the iframe
        driver.switch_to.frame(iframe_technical)

        # Assuming that the structure inside the iframe is similar to the previous one
        text_area_technical = driver.find_element(
                By.XPATH, "//body[@class='cke_editable cke_editable_themed cke_contents_ltr cke_show_borders']")
        text_area_technical.clear()
        text_area_technical.send_keys(fabric_technical_information)

        # Switch back to the main content
        driver.switch_to.default_content()

        #SCROLL TO TOP OF THE PAGHE AND PRESS SAVE
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)  # Wait for the page to scroll

        # Click the "Save" button
        save_button = driver.find_element(
                By.XPATH, "//button[contains(text(), 'Save')]")
        save_button.click()






        # new_url = "https://www.emeraldblindsandcurtains.co.uk/z-admin/products/view/5031/"
        # driver.get(new_url)

        #CLICK PRICING TABLE AGAIN
        element = driver.find_element(By.XPATH, '//a[@class="tab-link"]/strong[text()="Pricing"]')

        # Interact with the element (e.g., click)
        element.click()

        #SCROLL TO REPLCEMENT SLATS PRICING MATRIX
        # Scroll to the section containing the specified div
        section_element = driver.find_element(
                By.XPATH, "//div[div/div/p/strong[text()='Replacement Vertical Slats ']]")
        driver.execute_script("arguments[0].scrollIntoView();", section_element)

        # Use WebDriverWait to ensure the link is clickable
        wait = WebDriverWait(driver, 10)
        link_element = wait.until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="tabPricing"]/div[7]/div[2]/a'))
        )
        driver.execute_script("arguments[0].click();", link_element)

        #SELECT PRICE BAND FOR SLATS
        # Wait for the dropdown to be clickable
        vert_band_selector = (By.XPATH, '/html/body/section/div[2]/div/div[2]/form/div[2]/div[2]/div[5]/div[1]/div/span/span[1]/span/span[2]')
        dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(vert_band_selector))

        # Click the dropdown to open it
        dropdown.click()
        time.sleep(2)

        # Locate and click the "Vertical Slats Only 89mm Band B" option
        option_locator = (By.XPATH, '//li[text()="Vertical Slats Only 89mm Band B"]')
        option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(option_locator))
        option.click()
        time.sleep(2)

        #SCROLL TO TOP OF THE PAGE AND PRESS "SAVE CHANGES"
        # Scroll to the top of the page
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)  # Wait for the page to scroll

        # Click the "Save Changes" button
        save_changes = driver.find_element(By.XPATH, "//input[contains(@value, 'Save Changes')]")
        save_changes.click()
        time.sleep(2)



# Sample list of products
products = [
    {"product_name": "QUINTON BLACKOUT CALICO", "colors": ["Naturals"]},
    {"product_name": "QUINTON BLACKOUT DUCKEGG", "colors": ["Duckegg"]},
    {"product_name": "QUINTON BLACKOUT LATTE", "colors": ["Naturals"]},
    {"product_name": "QUINTON BLACKOUT STEEL GREY", "colors": ["Grey"]},


   

    # ... add more products as needed
]

driver = webdriver.Chrome()

# Looping through the products to upload each one
for product in products:
    upload_product_to_site(driver, product["product_name"], product["colors"])

driver.quit()







