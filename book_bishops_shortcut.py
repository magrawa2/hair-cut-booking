import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException

def get_user_input():
    print("Enter appointment details:")
    date = input('Enter date (YYYY-MM-DD format, e.g., 2025-06-27): ')
    time_slot = input('Enter time slot (HH:MM format, e.g., 11:00): ')
    name = input('Enter your full name: ')
    email = input('Enter your email: ')
    phone = input('Enter your phone number: ')
    password = input('Enter your login password: ')
    return date, time_slot, name, email, phone, password

def book_shortcut(date, time_slot, name, email, phone, password):
    options = Options()
    options.add_argument("user-data-dir=/Users/manish/Cursor/HairCutBooking/selenium-profile")
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 20)
    try:
        print("Opening Bishops Cupertino page...")
        driver.get('https://bishops.co/locations/cupertino/')

        print("Trying to accept cookie dialog...")
        try:
            cookie_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(), 'Accept') or contains(text(), 'agree') or contains(text(), 'OK')]")
            ))
            cookie_button.click()
            print("Cookie dialog accepted.")
            time.sleep(1)
        except Exception:
            print("No cookie dialog found or could not click it.")

        print("Clicking 'BOOK AN APPOINTMENT'...")
        book_appt = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[translate(text(), 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ') = 'BOOK AN APPOINTMENT']")))
        book_appt.click()

        print("Waiting for new tab to open...")
        time.sleep(3)
        window_handles = driver.window_handles
        if len(window_handles) > 1:
            driver.switch_to.window(window_handles[-1])
            print("Switched to new tab.")
        else:
            print("No new tab detected, staying on current tab.")

        print("Looking for 'Short Cut' service card...")
        short_cut_cards = driver.find_elements(By.XPATH, "//div[@class='services-designation-card' and @data-name='Short Cut']")
        if short_cut_cards:
            print("'Short Cut' service card found.")
            book_btn = short_cut_cards[0].find_element(By.XPATH, ".//a[contains(@class, 'btn') and contains(text(), 'Book')]")
            book_btn.click()
            print("'Book' button clicked for 'Short Cut'.")
        else:
            print("'Short Cut' service card not found. It may already be selected. Skipping this step.")

        # Click both 'Continue' buttons
        for i in range(2):
            print(f"Waiting for 'Continue' button #{i+1}...")
            continue_btn = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Continue')]"))
            )
            continue_btn.click()
            print(f"'Continue' button #{i+1} clicked.")
            time.sleep(1)

        # Click the <a> 'Confirm' button after Continue #2
        print("Waiting for 'Confirm' button after Continue #2...")
        confirm_btn_pre_date = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'btn') and contains(@class, 'btn-danger') and contains(text(), 'Confirm')]"))
        )
        confirm_btn_pre_date.click()
        print("'Confirm' button clicked after Continue #2.")
        time.sleep(1)

        # Wait for sign-in form
        print("Checking for sign-in form (optional)...")
        try:
            username_input = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@type='email' or @name='username' or @placeholder='Email']"))
            )
            password_input = driver.find_element(By.XPATH, "//input[@type='password']")
            username_input.clear()
            username_input.send_keys(email)
            password_input.clear()
            password_input.send_keys(password)
            # Click the sign-in button
            sign_in_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Sign In') or contains(text(), 'Log In') or contains(text(), 'Login')]")
            sign_in_btn.click()
            print("'Sign In' button clicked.")
            time.sleep(2)
        except TimeoutException:
            print("Sign-in form not present, continuing with booking flow.")

        # Wait for date picker
        print("Waiting for date picker...")
        date_picker = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "ui-datepicker"))
        )

        # Extract day from the provided date
        day = date.split('-')[2]
        print(f"Selecting day {day} in the date picker...")
        date_element = wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//a[text()='{day}' and contains(@class, 'ui-state-default')]"))
        )
        print(f"date_{day} displayed:", date_element.is_displayed())
        print(f"date_{day} enabled:", date_element.is_enabled())
        print(f"date_{day} classes:", date_element.get_attribute('class'))
        driver.execute_script("arguments[0].scrollIntoView(true);", date_element)
        driver.execute_script("arguments[0].click();", date_element)
        print(f"Clicked day {day} in the date picker (via JS).")
        time.sleep(1)

        # Proceed to time slot selection using user-provided time
        print(f"Selecting {time_slot} time slot...")
        try:
            label = wait.until(
                EC.element_to_be_clickable((By.XPATH, f"//label[@for='{time_slot}']"))
            )
            label.click()
            print(f"Clicked label for {time_slot} time slot.")
        except Exception as e:
            print(f"Label for {time_slot} not clickable, trying input directly...")
            all_slots = driver.find_elements(By.XPATH, "//input[contains(@class, 'slot_timings')]")
            for slot in all_slots:
                if slot.get_attribute('id') == time_slot and slot.is_displayed() and slot.is_enabled():
                    driver.execute_script("arguments[0].scrollIntoView(true);", slot)
                    slot.click()
                    print(f"Clicked input for {time_slot} time slot.")
                    break
            else:
                print(f"{time_slot} time slot not found or not clickable.")

        # After selecting the time slot...

        # Step 1: Click the "Continue" button
        print("Waiting for final 'Continue' button after time selection...")
        final_continue_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Continue')]"))
        )
        final_continue_btn.click()
        print("Final 'Continue' button clicked.")

        # After clicking the final "Continue" button...

        # 1. Check the cancellation policy checkbox
        print("Waiting for cancellation policy checkbox...")
        policy_checkbox = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='checkbox' and @name='conditions' and @id='conditions']"))
        )
        policy_checkbox.click()
        print("Checked the cancellation policy box.")
        time.sleep(1)  # Give UI a moment to enable the button

        # 2. Click the final "Confirm" button (as <a>)
        print("Waiting for final 'Confirm' button (as <a> tag)...")
        final_confirm_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'confirm-btn') and contains(text(), 'Confirm')]"))
        )
        final_confirm_btn.click()
        print("Final 'Confirm' button clicked.")

        # 3. Wait for confirmation message
        print("Waiting for confirmation message...")
        confirmation = wait.until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'confirmed') or contains(text(), 'Thank you') or contains(text(), 'success')]"))
        )
        print('Booking successful! Confirmation:', confirmation.text)

        time.sleep(1)  # Give the UI a moment to render
        all_slots = driver.find_elements(By.XPATH, "//input[contains(@class, 'slot_timings')]")
        print(f"Found {len(all_slots)} time slot radio buttons.")
        for idx, slot in enumerate(all_slots):
            print(f"Slot {idx}: id={slot.get_attribute('id')}, value={slot.get_attribute('value')}, displayed={slot.is_displayed()}, enabled={slot.is_enabled()}")
    except Exception as e:
        import traceback
        print('Booking failed:', e)
        traceback.print_exc()
    finally:
        driver.quit()

if __name__ == '__main__':
    date, time_slot, name, email, phone, password = get_user_input()
    book_shortcut(date, time_slot, name, email, phone, password) 