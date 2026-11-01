# Verification report — Ocloo Connector for Shopify

Date: 2026-11-02
Target: Odoo 19.0 (Community/Enterprise), PostgreSQL 16, Python 3.12
Method: Odoo test runner (`--test-enable --test-tags=/<module>`) in a throw-away container with
only the built module in its addons path, on databases created for the run and dropped afterwards.

## Results

| Module | Version | Tests | Failed | Errors |
|---|---|---|---|---|
| `mirak_shopify_connector_trial` (trial) | 19.0.1.0.0 | 28 | 0 | 0 |
| `mirak_shopify_connector` (full) | 19.0.2.0.3 | 24 | 0 | 0 |

Both runs installed the module from the ZIP in `dist/`, on an empty database — the same path a
customer or a store reviewer uses.

## What the suites cover

* A fake Shopify Admin API that records every GraphQL call and answers with realistic payloads,
  so the whole synchronization runs without a Shopify store, a network connection or a paid plan.
* Catalog: products and variants, prices, compare-at prices, SKU and barcodes, images, tags,
  collections, metafields.
* Stock: location to warehouse mapping, quantities in both directions, safety buffer.
* Orders: import as confirmed sales orders, customers, addresses, shipping, discounts, taxes,
  order edits, cancellations.
* Money: invoices, payments per method, refunds as credit notes, payouts.
* Trial edition: the 25-product ceiling, the single-store rule and the 30-day clock, each raising
  a clear message instead of silently stopping.

## Changes applied to the sources

1. **License key disabled for the store edition.** The paid source ships
   `LICENSE_KEY_REQUIRED = True` (a key per Shopify store for direct sales). The Odoo Apps Store
   edition must work on purchase alone, so every full module here is built with
   `LICENSE_KEY_REQUIRED = False`; the store status then reads "Odoo Apps edition" and no key is
   asked for.
2. **Branding.** Author, maintainer and copyright are Ocloo; the support address is
   `contact@ocloo.tech`; the contact constant used in the module messages is
   `contact@ocloo.tech` / `+974 6699 9180`; the OPL-1 documentation links point at the right Odoo
   series.
3. **Store assets.** New 512 px icon and 1120x560 banner per edition (Ocloo, phone number,
   trial/full badge), a full `static/description/index.html` page per edition and a `README.rst`.
4. **Manifest.** Name, summary, price (0 vs 99), author, support, website and the `images` list
   reduced to the files that actually exist.

## Static verification (all 12 modules)

* Python compilation of 414 files: no syntax error.
* XML well-formedness of every view and data file: no error.
* Manifest: version, price, author, every `data` entry and every `images` entry exists.
* Full edition: no module still carries `LICENSE_KEY_REQUIRED = True`.

## Limitations

* Only Odoo 19 could be executed here. Modules for 17, 18, 20, 21 and 22 were produced from the
  existing per-version sources (17/18/20) or from the 20 source (21/22) and verified statically.
* Odoo 21 and 22 were not released when these packages were built.
* No real Shopify store was contacted: the connector is covered with a mocked Admin API. A live
  test needs a Shopify store, an Admin API token and an HTTPS domain for the webhooks.
