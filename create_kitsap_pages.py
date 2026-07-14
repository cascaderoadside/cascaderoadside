#!/usr/bin/env python3
"""Generate Kitsap County zip code landing pages with Narrows Bridge surcharge."""

import os

kitsap_zips = [
    {"zip": "98367", "city": "Port Orchard"},
    {"zip": "98310", "city": "Bremerton"},
    {"zip": "98311", "city": "Bremerton"},
    {"zip": "98312", "city": "Bremerton"},
    {"zip": "98314", "city": "Bremerton"},
    {"zip": "98337", "city": "Gorst"},
    {"zip": "98383", "city": "Silverdale"},
    {"zip": "98370", "city": "Poulsbo"},
]

template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Roadside Assistance {city} WA {zip} | Cascade Roadside | (253) 322-5282</title>
    <meta name="description" content="24/7 roadside assistance in {city}, WA {zip}. Fast lockout, tire, jump start & fuel delivery service. Call (253) 322-5282 now.">
    <meta name="robots" content="index, follow">
    <meta property="og:title" content="Roadside Assistance {city} WA {zip} | Cascade Roadside | (253) 322-5282">
    <meta property="og:description" content="24/7 roadside assistance in {city}, WA {zip}. Fast lockout, tire, jump start & fuel delivery service. Call (253) 322-5282 now.">
    <meta property="og:type" content="business.business">
    <link rel="canonical" href="https://cascaderoadside.com/zip/{zip}.html">
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background-color: #0a0e1a;
            color: #fff;
            line-height: 1.6;
        }}
        
        header {{
            background-color: #0a0e1a;
            border-bottom: 3px solid #C4962A;
            padding: 20px;
            text-align: center;
            margin-bottom: 40px;
        }}
        
        header .logo {{
            font-size: 24px;
            font-weight: bold;
            color: #C4962A;
            margin-bottom: 10px;
        }}
        
        header .tagline {{
            font-size: 14px;
            color: #ccc;
        }}
        
        nav {{
            display: flex;
            justify-content: center;
            gap: 20px;
            padding: 10px 0;
            font-size: 14px;
        }}
        
        nav a {{
            color: #C4962A;
            text-decoration: none;
        }}
        
        nav a:hover {{
            text-decoration: underline;
        }}
        
        main {{
            max-width: 800px;
            margin: 0 auto;
            padding: 0 20px 40px;
        }}
        
        h1 {{
            font-size: 32px;
            margin-bottom: 20px;
            color: #C4962A;
        }}
        
        .tagline-section {{
            font-size: 18px;
            margin-bottom: 30px;
            color: #ddd;
            font-style: italic;
        }}
        
        .cta-button {{
            display: inline-block;
            background-color: #C4962A;
            color: #0a0e1a;
            padding: 18px 40px;
            font-size: 18px;
            font-weight: bold;
            text-decoration: none;
            border-radius: 8px;
            margin-bottom: 40px;
            transition: all 0.3s ease;
        }}
        
        .cta-button:hover {{
            background-color: #fff;
            box-shadow: 0 4px 12px rgba(196, 150, 42, 0.4);
        }}
        
        .surcharge-notice {{
            background-color: rgba(220, 53, 69, 0.1);
            border-left: 4px solid #dc3545;
            padding: 15px;
            margin-bottom: 30px;
            border-radius: 4px;
        }}
        
        .surcharge-notice p {{
            color: #ff9999;
            font-weight: 500;
            margin: 5px 0;
        }}
        
        .services {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 40px;
        }}
        
        .service {{
            background-color: rgba(255, 255, 255, 0.05);
            border: 2px solid #C4962A;
            border-radius: 8px;
            padding: 20px;
            text-align: center;
        }}
        
        .service h3 {{
            font-size: 18px;
            margin-bottom: 10px;
            color: #C4962A;
        }}
        
        .service .price {{
            font-size: 24px;
            font-weight: bold;
            color: #fff;
        }}
        
        .service .surcharge {{
            font-size: 12px;
            color: #ff9999;
            margin-top: 8px;
        }}
        
        .info-section {{
            background-color: rgba(255, 255, 255, 0.05);
            border-left: 4px solid #C4962A;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 4px;
        }}
        
        .info-section h2 {{
            font-size: 20px;
            margin-bottom: 10px;
            color: #C4962A;
        }}
        
        .info-section p {{
            margin-bottom: 8px;
        }}
        
        footer {{
            text-align: center;
            padding: 20px;
            border-top: 1px solid #C4962A;
            margin-top: 40px;
            color: #aaa;
            font-size: 12px;
        }}
        
        footer a {{
            color: #C4962A;
            text-decoration: none;
        }}
        
        footer a:hover {{
            text-decoration: underline;
        }}
        
        @media (max-width: 600px) {{
            h1 {{
                font-size: 24px;
            }}
            
            .services {{
                grid-template-columns: 1fr;
            }}
            
            .cta-button {{
                width: 100%;
                text-align: center;
            }}
            
            header {{
                padding: 15px;
            }}
        }}
    </style>
</head>
<body>
    <header>
        <div class="logo">Cascade Roadside</div>
        <div class="tagline">On the road when you need us.</div>
        <nav>
            <a href="https://cascaderoadside.com">Home</a>
            <a href="https://cascaderoadside.com/service-areas.html">Service Areas</a>
            <a href="tel:2533225282">(253) 322-5282</a>
        </nav>
    </header>
    
    <main>
        <h1>24/7 Roadside Assistance in {city}, WA ({zip})</h1>
        <p class="tagline-section">Fast, reliable roadside assistance 24/7 in your area.</p>
        
        <a href="tel:2533225282" class="cta-button">📞 Call Now: (253) 322-5282</a>
        
        <div class="surcharge-notice">
            <p>⚠️ <strong>Narrows Bridge Crossing Surcharge</strong></p>
            <p>Service to Kitsap County requires crossing the Tacoma Narrows Bridge. A surcharge of <strong>+$10</strong> applies to all service calls in this area.</p>
        </div>
        
        <div class="info-section">
            <h2>Our Services</h2>
            <p>We're here when you need us most. Fast response times, transparent pricing.</p>
        </div>
        
        <div class="services">
                <div class="service">
                    <h3>Lockouts</h3>
                    <p class="price">$95</p>
                    <p class="surcharge">+ $10 Narrows Bridge</p>
                </div>
                <div class="service">
                    <h3>Flat Tire</h3>
                    <p class="price">$95</p>
                    <p class="surcharge">+ $10 Narrows Bridge</p>
                </div>
                <div class="service">
                    <h3>Jump Start</h3>
                    <p class="price">$85</p>
                    <p class="surcharge">+ $10 Narrows Bridge</p>
                </div>
                <div class="service">
                    <h3>Fuel Delivery</h3>
                    <p class="price">$95</p>
                    <p class="surcharge">+ $10 Narrows Bridge</p>
                </div>
        </div>
        
        <div class="info-section">
            <h2>Why Choose Cascade Roadside?</h2>
            <p>✓ 24/7 availability</p>
            <p>✓ Professional technicians</p>
            <p>✓ Transparent, upfront pricing (including Narrows Bridge surcharge)</p>
            <p>✓ Fast response times in {city}, WA</p>
            <p>✓ After-hours surcharge: +$35 (8 PM–7 AM)</p>
        </div>
        
        <div class="info-section">
            <h2>Contact Us</h2>
            <p><strong>Phone:</strong> <a href="tel:2533225282" style="color: #C4962A;">(253) 322-5282</a></p>
            <p><strong>Service Area:</strong> {city}, WA {zip} (Kitsap County)</p>
            <p><strong>Hours:</strong> 24/7</p>
        </div>
    </main>
    
    <footer>
        <p>&copy; 2026 Cascade Roadside LLC. All rights reserved.</p>
        <p><a href="https://cascaderoadside.com">cascaderoadside.com</a></p>
    </footer>
    
    <script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Cascade Roadside LLC",
  "telephone": "(253) 322-5282",
  "url": "https://cascaderoadside.com",
  "areaServed": {{
    "@type": "PostalCodeRange",
    "postalCode": "{zip}"
  }},
  "address": {{
    "@type": "PostalAddress",
    "addressLocality": "{city}",
    "addressRegion": "WA",
    "postalCode": "{zip}",
    "addressCountry": "US"
  }},
  "serviceType": [
    "Lockout Service",
    "Tire Service",
    "Jump Start Service",
    "Fuel Delivery"
  ]
}}
    </script>
</body>
</html>
'''

zip_dir = "/Users/dougwinker/.openclaw/workspace/cascade-roadside/zip"
os.makedirs(zip_dir, exist_ok=True)

for item in kitsap_zips:
    filename = os.path.join(zip_dir, f"{item['zip']}.html")
    content = template.format(city=item['city'], zip=item['zip'])
    with open(filename, 'w') as f:
        f.write(content)
    print(f"Created {filename}")

print(f"\nCreated {len(kitsap_zips)} Kitsap County zip pages")
