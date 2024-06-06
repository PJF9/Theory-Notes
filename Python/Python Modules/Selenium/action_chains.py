"""
    Action Chains gives us more options to work with selenium.

    When we call methods for actions on the ActionChains object, 
    the actions are stored in a queue in the ActionChains object. 
    When we call perform(), the events are fired in the order 
    they are queued up.

    The actions that we can perform are:
        click(on_element=None): Clicks an element.
            (on_element): The element we want to click. If None
                clicks on currect mouse position.

        click_and_hold(on_element=None): Holds down the left mouse
        button on an element.
            (on_element): The element to mouse down. If None, clicks 
                on current mouse position.

        context_click(on_element=None): Performs a right click 
        on an element.
            (on_element): The element to context-click. If None, 
                clicks on current mouse position.

        double_click(on_element=None): Double-clicks an element.
            (on_element): The element to double-click. If None, 
                clicks on current mouse position.

        drag_and_drop(source, target): Holds down the left mouse button 
        on the source element, then moves to the target element and
        releases the mouse button.
            (source): The element to mouse down.
            (target): The element to mouse up.

        key_down(value, element=None): Sends a key press only, without 
        releasing it. Should only be used with modifier keys (Control, Alt and Shift). 
            (value): The modifier key to send. Values are defined in Keys class.
            (element): The element to send keys. If None, sends a key to current
                focused element.

        key_up(value, element=None): Releases a modifier key.
            (value): The modifier key to send. Values are defined in Keys class.
            (element): The element to send keys. If None, sends a key to current 
                focused element.

        move_to_element(to_element): Moving the mouse to the middle of an element.
            (to_element): The WebElement to move to.

        pause(seconds): Pause all inputs for the specified duration in seconds

        release(on_element=None): Releasing a held mouse button on an element.
            (on_element): The element to mouse up. If None, releases on current 
                mouse position.
     
        reset_actions(): Clears actions that are already stored locally and on the 
        remote end
    
        send_keys(*keys_to_send): Sends keys to current focused element.
            (keys_to_send): The keys to send. Modifier keys constants can be found in 
                the ‘Keys’ class.

    send_keys_to_element(element, *keys_to_send): Sends keys to an element.
        (element): The element to send keys.
        (keys_to_send): The keys to send. Modifier keys constants can be found in the 
            ‘Keys’ class.
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

path = "C:\\Program Files\\Mozilla Firefox\\geckodriver.exe"

driver = webdriver.Firefox(executable_path=path)
driver.get("https://orteil.dashnet.org/cookieclicker/")

""" With this line of code the program pause for 7 seconds. """
driver.implicitly_wait(7)

""" Creating the action object. """
actions = ActionChains(driver)

""" Cooking terms. """
close = driver.find_element_by_link_text("Got it!")
close.click()

""" Getting some data from the site. """
cookie = driver.find_element_by_id("bigCookie")
products = [driver.find_element_by_id("productPrice" + str(i)) for i in range(4)]

""" Decalre some actions """
actions.move_to_element(cookie)
actions.double_click()

while True:
    actions.perform()

    """ Creating the accual bot experiment. """
    cookies = int(driver.find_element_by_id("cookies").text.split(' ')[0])
    for product in products[::-1]:
        try:
            if cookies >= int(product.text):
                upgrade_actions = ActionChains(driver)
                upgrade_actions.move_to_element(product)
                upgrade_actions.click()
                upgrade_actions.perform()
        except ValueError:
            pass
