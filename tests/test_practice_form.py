import os.path
from datetime import datetime
from selene import browser, have, be, command
import time

def test_fill_practice_form():
    browser.open('/')

    browser.element('[class="close"]').perform(command.js.click)

    '''Добавление в корзину через каталог'''

    browser.element('[data-test-id="button__catalog"]').click() #поиск по каталогу
    time.sleep(5)

    browser.element('[id="filters"]>[href="/category/khobbi-i-tvorchestvo-10008"]').click() #  поиск в каталоге по "Детские товары"

   # browser.element('[id="filters"] [data-test-id="checkbox__filter"]')[237].click() # поиск по бренду LEGO

    # browser.element('').perform(command.js.scroll_into_view).should(be.visible) # добавить скролл
    #
    # browser.all('[data-test-id="text__product-name"]')[0].should(
    #     have.text('Конструктор LEGO Architecture, 21054, "Белый дом"')).click()
    # browser.element('[data-test-id="button__add-cart"]').click()
    # browser.element('[class="cart-enter"]').click()
    #
    #
    # ''' Добавление в корзину через поиск'''
    # browser.element('[class="default-input"]').type('Конструктор LEGO Architecture').press_enter()
    # browser.all('[data-test-id="text__product-name"]')[0].should(
    #     have.text('Конструктор LEGO Architecture, 21054, "Белый дом"')).click()
    # browser.element('[data-test-id="button__add-cart"]').click()
    # browser.element('[class="cart-enter"]').click()
    #
    # '''Добавление в корзину через страницу избранное'''
    # browser.element('class="ui-link action-button"').click()
    # browser.element('[data-test-id="button__add-to-cart" ]').click()



    #browser.all('[data-test-id="text__price"]')[0].locate().text

    # browser.all('[data-test-id="text__price"]')[0].should(have.text('651 ₽'))
    # browser.all('[data-test-id="text__product-name"]')[0].locate().text
    # browser.all('[data-test-id="text__old-price"]')[0].locate().text

    # browser.all('[data-test-id="text__product-name"]')[0].locate().text
    # browser.all('[data-test-id="text__product-name"]')[0].should(
    #     have.text('Конструктор Звездные Войны (Star Wars) Звездный разрушитель / Истребитель / Венатор'))
    # time.sleep(5)



