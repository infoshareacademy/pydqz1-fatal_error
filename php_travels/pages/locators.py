from selenium.webdriver.common.by import By


class CommonSignInLocators:
    MY_ACCOUNT_MENU = (By.CSS_SELECTOR, "ul .nav #li_myaccount")
    SIGN_UP_LINK = (By.CSS_SELECTOR, ".open >ul>:nth-child(2) > a")
    NAME_INPUT = (By.CSS_SELECTOR, "[name='firstname']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "[name='lastname']")
    PHONE_INPUT = (By.CSS_SELECTOR, "[name='phone']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "[name='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "[name='password']")
    CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "[name='confirmpassword']")
    SIGN_UP_BUTTON = (By.CSS_SELECTOR, "button.signupbtn.btn_full.btn.btn-action.btn-block.btn-lg")
    MY_PROFILE_TEXT = (By.CSS_SELECTOR, "div#body-section li:nth-child(2) > a")
