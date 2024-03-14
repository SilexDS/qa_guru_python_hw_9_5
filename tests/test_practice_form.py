import os.path
from datetime import datetime
from selene import browser, have, be, command, by
import time

def test_fill_practice_form():
    browser.open('/')



    ''' Добавление в корзину через поиск'''


    browser.element('[class="_input_1su1z_19 _inputShown_1su1z_43"]').type('dress').press_enter()
    browser.element('[id="MP002XW1CDIT"]').with_(timeout=120).click()
    browser.element('[class="x-button x-button_primaryPremium x-button_48 _cartButton_lrjtr_11"]').click().with_(timeout=120)
    browser.element('[class="_firstRow_1widv_194"]').click()
    browser.element('[class="x-button x-button_primaryFilledWeb7184 x-button_32 x-button_link x-button_link_32 x-button_intrinsic-width"]').click()
    browser.element('[class="_value_1oots_21"]').should(have.text('15 990 ₽'))

    '''Удаление товара из корзины'''

    ''' Добавление в корзину через каталог'''
    browser.element('').click() #не получилось добавить через каталог, пункт Одежда
    browser.element('[class="_title_1ejii_15"]').should(have.text('Premium')).click()







