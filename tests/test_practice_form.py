import os.path
from datetime import datetime
from selene import browser, have, be, command, by
import time

def test_fill_practice_form():
    browser.open('/')

    # browser.element('[class="close"]').perform(command.js.click)
    # time.sleep(2)

    '''Добавление в корзину через каталог'''

    browser.element('[data-test-id="button__catalog"]').click() #поиск по каталогу
    browser.element('aside').element(by.text("Детские товары")).click()
    time.sleep(3)
    browser.all('[data-test-id="text__product-name"]')[2].should(
        have.text('Игрушка-подушка "Гусь-обнимусь", с пледом подарок на 8 марта девушке')).click() #переход в карточку Игрушка-подушка "Гусь-обнимусь"
    time.sleep(3)
    browser.all('[class="background"]')[0].click() #выбор цвета товара
    browser.element('[data-tooltip="ГУСЬ С ПЛЕДОМ 90 СМ"]').click().perform(command.js.scroll_into_view) #размер товара
    time.sleep(1)
    browser.element('[data-test-id="button__add-cart"]').click() #добавление товара в корзину
    time.sleep(2)
    browser.element('[class="cart-enter"]').click() #переход в корзину
    browser.element('[data-test-id="text__full-price"]').should(have.text('2 000 ₽')) #проверка по цене
    time.sleep(3)

    ''' Добавление в корзину через поиск'''

    browser.element('[data-test-id="input__search"]').type('Игрушка-подушка Гусь-обнимусь').press_enter()
    time.sleep(2)
    browser.all('[data-test-id="text__product-name"]')[0].should(
        have.text('Игрушка-подушка "Гусь-обнимусь", с пледом подарок на 8 марта девушке')).click()
    browser.all('[class="background"]')[0].click() #выбор цвета товара
    browser.element('[data-tooltip="ГУСЬ С ПЛЕДОМ 90 СМ"]').click().perform(command.js.scroll_into_view) #размер товара
    time.sleep(1)
    browser.element('[data-test-id="button__add-cart"]').click() #добавление товара в корзину
    time.sleep(2)
    browser.element('[class="cart-enter"]').click() #переход в корзину
    browser.element('[data-test-id="text__product-price"]').should(have.text('4 000 ₽')) # проверка по цене



    '''Добавление в корзину через страницу избранное'''
    browser.element('[data-test-id="button__catalog"]').click() # поиск по каталогу
    browser.element('aside').element(by.text("Детские товары")).click()
    time.sleep(3)
    browser.all('[data-test-id="text__product-name"]')[2].should(
        have.text('Игрушка-подушка "Гусь-обнимусь", с пледом подарок на 8 марта девушке')).click()
    browser.all('[class="noselect product-card-like"]')[0].click()

    browser.element('[data-test-id="button__wishes"]').click() # переход во вкладку избранное
    # time.sleep(3)
    # browser.element('[data-test-id="text__product-price"]').should(have.text('4 000 ₽'))  # проверка по цене
    # #
    # '''Очистка корзины и проверка , что корзина пуста'''
    # browser.element('[data-test-id="button__delete-from-cart"]').click()










  # browser.all('[data-test-id="button__show-more"]')[1].click()

    #browser.element(by.text("LEGO")).element('./..').click()
    # time.sleep(5)


#  browser.element('[id="filters"]>[href="/category/khobbi-i-tvorchestvo-10008"]').click() #  поиск в каталоге по "Детские товары"

   # browser.element('[id="filters"] [data-test-id="checkbox__filter"]')[237].click() # поиск по бренду LEGO

    # browser.element('').perform(command.js.scroll_into_view).should(be.visible) # добавить скролл
    #
    # browser.all('[data-test-id="text__product-name"]')[0].should(
    #     have.text('Конструктор LEGO Architecture, 21054, "Белый дом"')).click()
    # browser.element('[data-test-id="button__add-cart"]').click()
    # browser.element('[class="cart-enter"]').click()
    #
    # #
    # ''' Добавление в корзину через поиск'''
    # browser.element('[class="default-input"]').type('Игрушка-подушка Гусь-обнимусь').press_enter()
    #
    # browser.all('[data-test-id="text__product-name"]')[1].click()
    # browser.element('[data-test-id="button__add-cart"]').click()
    # browser.element('[class="cart-enter"]').click()
    # #
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

   # browser.all('[data-test-id="text__product-name"]')[1].should(
   #      have.text('Конструктор LEGO Architecture, 21054, "Белый дом"')).click()
   #  browser.element('[data-test-id="button__add-cart"]').click()
   #  browser.element('[class="cart-enter"]').click()
   #  #

