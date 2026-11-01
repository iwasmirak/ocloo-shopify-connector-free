Ocloo Connector for Shopify (Free Trial)
========================================

Odoo 21.0 — Community and Enterprise
Version: 21.0.1.0.0
Author: Ocloo
Support: contact@ocloo.tech — WhatsApp +974 6699 9180
Price: Free (25 products, 1 store, 30 days)
License: OPL-1

Two-way synchronization between Odoo and one or several Shopify stores.

* 25 linked products, one Shopify store, 30 days counted from the installation.
* Every feature of the connector is available during the trial.

Features
--------

* Products and variants, prices and compare-at prices, Shopify Markets prices, SKU and barcodes,
  descriptions, status, image galleries, tags, product types, collections, metafields, translations.
* Stock of several Shopify locations kept in line with Odoo warehouses, in both directions, with a
  safety buffer and a percentage.
* Shopify orders imported as confirmed sales orders with customers, addresses, shipping, discounts
  and taxes; order edits, POS orders and cancellations in both directions.
* Customers both ways, abandoned checkouts as CRM opportunities.
* Invoices, payments per payment method, refunds as credit notes, returns both ways, Shopify
  Payments payouts with fees and reconciliation.
* Deliveries validated in Odoo are fulfilled in Shopify (or the opposite).
* Real-time updates through webhooks, an OAuth install link, a dashboard and detailed logs.

Requirements
------------

* Odoo 21.0 with Sales, Inventory and Invoicing.
* A Shopify store with Admin API access; Python ``cryptography``.
* An HTTPS domain reachable by Shopify for the webhooks.

Installation
------------

1. Copy the module folder into your addons path and restart Odoo.
2. Update the apps list and install the module.
3. Create a store record: shop domain, access token (or the OAuth install link), warehouse.
4. Set the synchronization options, then run the first synchronization and follow the dashboard.

Ocloo — contact@ocloo.tech — WhatsApp +974 6699 9180 — https://ocloo.tech
