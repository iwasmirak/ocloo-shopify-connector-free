# Ocloo Connector for Shopify — Free Trial

Two-way synchronization between Odoo and Shopify: products, variants, images, tags, collections,
multi-location stock, orders, customers, invoices, payments, payouts, refunds and returns, with
real-time webhooks, a dashboard and detailed logs.

This repository holds the **free trial** of the connector for Odoo 17, 18, 19, 20, 21 and 22.

## What the trial does

* **Catalog**: products and variants, prices and compare-at prices, Shopify Markets prices, SKU
  and barcodes, descriptions, status, image galleries, tags, collections, metafields, translations.
* **Stock**: each Shopify location follows an Odoo warehouse, in both directions, with a safety
  buffer and a percentage; deliveries validated in Odoo fulfil the order in Shopify.
* **Orders and customers**: orders imported as confirmed sales orders with addresses, shipping,
  discounts and taxes; edits, POS orders, cancellations, abandoned checkouts as CRM opportunities.
* **Money**: invoices, payments per payment method, refunds as credit notes, Shopify Payments
  payouts with fees and reconciliation.
* **Returns** both ways, **real-time webhooks**, one log line per API call, retries and a dashboard.

## Limits of the trial

* **25 linked products**, **one Shopify store**, **30 days** counted from installation.
* Every feature of the connector is available during the trial — only the volume and the duration
  are limited. The full edition removes all three limits.

## Branches

Each Odoo series has its own branch, with the module folder at the root:

| Branch | Odoo | Module |
|---|---|---|
| [`17.0`](../../tree/17.0) | 17.0 | `mirak_shopify_connector_trial` |
| [`18.0`](../../tree/18.0) | 18.0 | `mirak_shopify_connector_trial` |
| [`19.0`](../../tree/19.0) | 19.0 | `mirak_shopify_connector_trial` |
| [`20.0`](../../tree/20.0) | 20.0 | `mirak_shopify_connector_trial` |
| [`21.0`](../../tree/21.0) | 21.0 | `mirak_shopify_connector_trial` |
| [`22.0`](../../tree/22.0) | 22.0 | `mirak_shopify_connector_trial` |

Ready-to-install archives are attached to the [latest release](../../releases/latest).

## Installation

1. Download the ZIP for your Odoo version, or clone the matching branch.
2. Copy the `mirak_shopify_connector_trial` folder into your addons path and restart Odoo.
3. Update the apps list and install **Ocloo Connector for Shopify (Free Trial)**.
4. Create a store record: shop domain, Admin API token (or the OAuth install link), warehouse.
5. Run the first synchronization and follow the dashboard.

Requirements: Odoo with Sales, Inventory and Invoicing, Python `cryptography`, and an HTTPS domain
reachable by Shopify for the webhooks.

## Tests

The Odoo 19 suite of this edition runs 28 tests with no failure, against a fake Shopify Admin API
that records every GraphQL call. Modules for the other series are verified statically.

## Full edition

No product, store or time limit, and no license key to enter: buying the module on the Odoo Apps
Store is enough.

## Contact

Ocloo — contact@ocloo.tech — WhatsApp [+974 6699 9180](https://wa.me/97466999180) — https://ocloo.tech

License: OPL-1 (Odoo Proprietary License v1.0). © 2026 Ocloo. Shopify is a trademark of Shopify Inc.;
this connector is independent and not affiliated with Shopify Inc.
