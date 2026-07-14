#!/usr/bin/env python3
"""Generate landing pages for all Cascade Roadside zip codes."""

import csv
import json
from pathlib import Path

# Business info
BUSINESS = {
    "name": "Cascade Roadside LLC",
    "phone": "(253) 322-5282",
    "phone_raw": "2533225282",
    "website": "cascaderoadside.com",
    "tagline": "On the road when you need us.",
    "colors": {
        "navy": "#0a0e1a",
        "orange": "#C4962A"
    }
}

SERVICES = [
    {"name": "Lockouts", "price": "$95"},
    {"name": "Flat Tire", "price": "$95"},
    {"name": "Jump Start", "price": "$85"},
    {"name": "Fuel Delivery", "price": "$95"}
]

def generate_zip_page(zipcode, city, state):
    """Generate HTML for a single zip code landing page."""
    
    title = f"Roadside Assistance {city} WA {zipcode} | Cascade Roadside | (253) 322-5282"
    meta_desc = f"24/7 roadside assistance in {city}, WA {zipcode}. Fast lockout, tire, jump start & fuel delivery service. Call {BUSINESS['phone']} now."
    h1 = f"24/7 Roadside Assistance in {city}, WA ({zipcode})"
    
    # Build service area JSON for schema.org
    service_area = {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "name": BUSINESS["name"],
        "telephone": BUSINESS["phone"],
        "url": f"https://{BUSINESS['website']}",
        "areaServed": {
            "@type": "PostalCodeRange",
            "postalCode": str(zipcode)
        },
        "address": {
            "@type": "PostalAddress",
            "addressLocality": city,
            "addressRegion": state,
            "postalCode": str(zipcode),
            "addressCountry": "US"
        },
        "serviceType": ["Lockout Service", "Tire Service", "Jump Start Service", "Fuel Delivery"]
    }
    
    services_html = "\n".join([
        f'                <div class="service">\n'
        f'                    <h3>{service["name"]}</h3>\n'
        f'                    <p class="price">{service["price"]}</p>\n'
        f'                </div>'
        for service in SERVICES
    ])
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{meta_desc}">
    <meta name="robots" content="index, follow">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{meta_desc}">
    <meta property="og:type" content="business.business">
    <link rel="canonical" href="https://{BUSINESS['website']}/zip/{zipcode}.html">
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background-color: {BUSINESS['colors']['navy']};
            color: #fff;
            line-height: 1.6;
        }}
        
        header {{
            background-color: {BUSINESS['colors']['navy']};
            border-bottom: 3px solid {BUSINESS['colors']['orange']};
            padding: 20px;
            text-align: center;
            margin-bottom: 40px;
        }}
        
        header .logo {{
            font-size: 24px;
            font-weight: bold;
            color: {BUSINESS['colors']['orange']};
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
            color: {BUSINESS['colors']['orange']};
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
            color: {BUSINESS['colors']['orange']};
        }}
        
        .tagline-section {{
            font-size: 18px;
            margin-bottom: 30px;
            color: #ddd;
            font-style: italic;
        }}
        
        .cta-button {{
            display: inline-block;
            background-color: {BUSINESS['colors']['orange']};
            color: {BUSINESS['colors']['navy']};
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
        
        .services {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 40px;
        }}
        
        .service {{
            background-color: rgba(255, 255, 255, 0.05);
            border: 2px solid {BUSINESS['colors']['orange']};
            border-radius: 8px;
            padding: 20px;
            text-align: center;
        }}
        
        .service h3 {{
            font-size: 18px;
            margin-bottom: 10px;
            color: {BUSINESS['colors']['orange']};
        }}
        
        .service .price {{
            font-size: 24px;
            font-weight: bold;
            color: #fff;
        }}
        
        .info-section {{
            background-color: rgba(255, 255, 255, 0.05);
            border-left: 4px solid {BUSINESS['colors']['orange']};
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 4px;
        }}
        
        .info-section h2 {{
            font-size: 20px;
            margin-bottom: 10px;
            color: {BUSINESS['colors']['orange']};
        }}
        
        .info-section p {{
            margin-bottom: 8px;
        }}
        
        footer {{
            text-align: center;
            padding: 20px;
            border-top: 1px solid {BUSINESS['colors']['orange']};
            margin-top: 40px;
            color: #aaa;
            font-size: 12px;
        }}
        
        footer a {{
            color: {BUSINESS['colors']['orange']};
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
        <div class="tagline">{BUSINESS['tagline']}</div>
        <nav>
            <a href="https://{BUSINESS['website']}">Home</a>
            <a href="https://{BUSINESS['website']}/service-areas.html">Service Areas</a>
            <a href="tel:{BUSINESS['phone_raw']}">{BUSINESS['phone']}</a>
        </nav>
    </header>
    
    <main>
        <h1>{h1}</h1>
        <p class="tagline-section">Fast, reliable roadside assistance 24/7 in your area.</p>
        
        <a href="tel:{BUSINESS['phone_raw']}" class="cta-button">📞 Call Now: {BUSINESS['phone']}</a>
        
        <div class="info-section">
            <h2>Our Services</h2>
            <p>We're here when you need us most. Fast response times, transparent pricing.</p>
        </div>
        
        <div class="services">
{services_html}
        </div>
        
        <div class="info-section">
            <h2>Why Choose Cascade Roadside?</h2>
            <p>✓ 24/7 availability</p>
            <p>✓ Professional technicians</p>
            <p>✓ Transparent, upfront pricing</p>
            <p>✓ Fast response times in {city}, WA</p>
            <p>✓ After-hours surcharge: +$35 (8 PM–7 AM)</p>
        </div>
        
        <div class="info-section">
            <h2>Contact Us</h2>
            <p><strong>Phone:</strong> <a href="tel:{BUSINESS['phone_raw']}" style="color: {BUSINESS['colors']['orange']};">{BUSINESS['phone']}</a></p>
            <p><strong>Service Area:</strong> {city}, WA {zipcode}</p>
            <p><strong>Hours:</strong> 24/7</p>
        </div>
    </main>
    
    <footer>
        <p>&copy; 2026 Cascade Roadside LLC. All rights reserved.</p>
        <p><a href="https://{BUSINESS['website']}">cascaderoadside.com</a></p>
    </footer>
    
    <script type="application/ld+json">
{json.dumps(service_area, indent=2)}
    </script>
</body>
</html>
"""
    return html

def main():
    # Read CSV
    zipcodes = []
    with open('/Users/dougwinker/.openclaw/workspace/cascade-roadside/service-area-zipcodes.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            zipcodes.append(row)
    
    # Generate HTML files
    output_dir = Path('/Users/dougwinker/.openclaw/workspace/cascade-roadside/zip')
    output_dir.mkdir(exist_ok=True, parents=True)
    
    for row in zipcodes:
        zipcode = row['zipcode']
        city = row['city']
        state = row['state']
        
        html = generate_zip_page(zipcode, city, state)
        output_file = output_dir / f"{zipcode}.html"
        output_file.write_text(html)
        print(f"✓ Created {zipcode}.html for {city}, WA")
    
    print(f"\n✓ Generated {len(zipcodes)} zip code landing pages")

if __name__ == '__main__':
    main()
