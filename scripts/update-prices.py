#!/usr/bin/env python3
"""
Fetch live Amazon prices via Rainforest API and update HTML files.
Called by GitHub Actions daily. See .github/workflows/update-prices.yml

Usage:
    RAINFOREST_API_KEY=xxx python3 scripts/update-prices.py
"""

import json, os, re, sys, urllib.request, time

API_KEY = os.environ.get('RAINFOREST_API_KEY', '')
if not API_KEY:
    print("ERROR: RAINFOREST_API_KEY not set")
    sys.exit(1)

# Products to track: (ASIN, files to update, price marker pattern)
PRODUCTS = [
    {
        'asin': 'B0DCK8P752',
        'name': 'Wavytalk Pro Steam Straightener',
        'files': [
            'wavytalk-pro-steam-straightener-review.html',
            'steam-straighteners.html',
            'index.html',
            'best-steam-straighteners-2026.html',
        ],
        'marker': 'data-price-steam',
    },
    {
        'asin': 'B09CP8SSGP',
        'name': 'Wavytalk Blown Away Ionic Hair Dryer',
        'files': [
            'wavytalk-ionic-hair-dryer-review.html',
            'hair-dryers.html',
            'index.html',
            'best-ionic-hair-dryers-2026.html',
        ],
        'marker': 'data-price-dryer',
    },
]


def fetch_price(asin: str) -> dict:
    """Fetch product price from Rainforest API."""
    url = f"https://api.rainforestapi.com/request?api_key={API_KEY}&type=product&asin={asin}&amazon_domain=amazon.com"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'HairToolsReview-PriceBot/1.0'})
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read())

        product = data.get('product', {})
        buybox = product.get('buybox_winner', {})

        price_val = buybox.get('price', {}).get('value')
        price_raw = buybox.get('price', {}).get('raw', '')
        rrp_val = buybox.get('rrp', {}).get('value')
        rrp_raw = buybox.get('rrp', {}).get('raw', '')

        return {
            'price': price_val,
            'price_raw': price_raw,
            'rrp': rrp_val,
            'rrp_raw': rrp_raw,
            'in_stock': buybox.get('availability', {}).get('type') == 'in_stock',
            'title': product.get('title', ''),
        }
    except Exception as e:
        print(f"  ERROR fetching {asin}: {e}")
        return {}


def update_price_in_file(filepath: str, marker: str, new_price: str):
    """Update data-price-xxx="$XX.XX" attribute, visible text, AND JSON-LD offers.price."""
    if not os.path.exists(filepath):
        return False

    content = open(filepath).read()

    # 1. Update the data-price attribute value
    attr_pattern = f'{marker}="[^"]*"'
    attr_replacement = f'{marker}="${new_price}"'
    new_content = re.sub(attr_pattern, attr_replacement, content)

    # 2. Update the visible price text inside the span
    span_pattern = rf'(<span {marker}="\$[\d.]+">)[^<]*(</span>)'
    span_replacement = rf'\g<1>${new_price}\g<2>'
    new_content = re.sub(span_pattern, span_replacement, new_content)

    # 3. Update JSON-LD offers.price (pattern: "price": "XX.XX" inside Offer block)
    # Only on review pages that have Product schema with offers
    new_content = re.sub(
        r'("@type":\s*"Offer"[^}]*"price":\s*")[^"]+(")',
        rf'\g<1>{new_price}\g<2>',
        new_content
    )

    if new_content != content:
        open(filepath, 'w').write(new_content)
        return True
    return False


def main():
    print(f"=== HairToolsReview Price Update ===")
    print(f"Time: {time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime())}")
    print()

    changes = 0

    for product in PRODUCTS:
        print(f"[{product['name']}] ASIN: {product['asin']}")
        result = fetch_price(product['asin'])

        if not result or not result.get('price'):
            print(f"  SKIP: No price returned")
            continue

        price = f"{result['price']:.2f}"
        print(f"  Current price: ${price}")
        if result.get('rrp'):
            print(f"  RRP: ${result['rrp']:.2f}")
        print(f"  In stock: {result.get('in_stock', 'unknown')}")

        for filepath in product['files']:
            updated = update_price_in_file(filepath, product['marker'], price)
            if updated:
                print(f"  Updated: {filepath}")
                changes += 1

        print()
        # Rate limit: wait between requests
        time.sleep(2)

    print(f"Total files updated: {changes}")
    return 0 if changes >= 0 else 1


if __name__ == '__main__':
    sys.exit(main())
