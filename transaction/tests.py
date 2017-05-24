# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.test import LiveServerTestCase
from django.urls import reverse

from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver

from .models import Transaction


# Create your tests here.
class TransactionDetailTest(LiveServerTestCase):

    def setUp(self):
        super(TransactionDetailTest, self).setUp()
        self.selenium = WebDriver()

    def tearDown(self):
        self.selenium.quit()
        super(TransactionDetailTest, self).tearDown()

    def test_detail_view_with_a_future_transaction(self):
        """
        Check if detail view of a new transaction is working
        """

        # create fake transaction
        future_transaction = Transaction.objects.create(
            trx_id='01023A9AC', address_ship='JALAN GURNEY',
            date_order='2017-05-24', seller_name='FURHAN',
            delivery_service='REX'
        )

        # test the index in view.py
        url = reverse('transaction:index', args=(future_transaction.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_has_same_value_with_database(self):
        """
        Check if the detail view of a new transaction is
        the same as in the database record
        """

        # create fake transaction
        future_transaction = Transaction.objects.create(
            trx_id='01023A9AB', address_ship='JALAN GURNEY',
            date_order='2017-05-24', seller_name='FURHA',
            delivery_service='REX'
        )

        # initialize selenium
        driver = self.selenium
        driver.implicitly_wait(30)
        driver.maximize_window()

        # access the server's URL [127.0.0.1:8000/transaction/]
        driver.get('%s%s%s' % (self.live_server_url, '/transaction/',
                               future_transaction.id))

        # get the values in UI
        trx_id_ui = driver.find_element_by_xpath("//p/span[@id='transaction_id']")
        seller_name_ui = driver.find_element_by_xpath("//p/span[@id='seller_name']")
        delivery_service_ui = driver.find_element_by_xpath("//p/span[@id='delivery_service']")
        date_order_ui = driver.find_element_by_xpath("//p/span[@id='date_order']")
        address_ship_ui = driver.find_element_by_xpath("//p/span[@id='address_ship']")

        # check if the values in UI has the same values in the database record
        self.assertEqual(trx_id_ui.text, future_transaction.trx_id)
        self.assertEqual(seller_name_ui.text, future_transaction.seller_name)
        self.assertEqual(delivery_service_ui.text, future_transaction.delivery_service)
        self.assertEqual(date_order_ui.text, future_transaction.date_order)
        self.assertEqual(address_ship_ui.text, future_transaction.address_ship)
