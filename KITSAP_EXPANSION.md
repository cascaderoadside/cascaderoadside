# Cascade Roadside — Kitsap County Expansion
**Completed: July 13, 2026**

## Summary
Successfully expanded Cascade Roadside service area to include Kitsap County (Tacoma Narrows Bridge crossing area) with proper pricing, landing pages, and interactive service area map.

## Changes Made

### 1. ✅ CSV Database Updated
- **File:** `service-area-zipcodes.csv`
- **Zips Added:** 9 new Kitsap County zip codes
- **Total Service Area:** 95 zip codes (was 86, +9)

### 2. ✅ Kitsap County Zip Codes Added
All Kitsap zips configured with **+$10 Narrows Bridge Crossing Surcharge**:

| Zip | City | County |
|-----|------|--------|
| 98366 | Port Orchard | Kitsap |
| 98367 | Port Orchard | Kitsap |
| 98310 | Bremerton | Kitsap |
| 98311 | Bremerton | Kitsap |
| 98312 | Bremerton | Kitsap |
| 98314 | Bremerton | Kitsap |
| 98337 | Gorst | Kitsap |
| 98383 | Silverdale | Kitsap |
| 98370 | Poulsbo | Kitsap |

### 3. ✅ Landing Pages Created (9 pages)
All zip pages include:
- Standard service pricing: $85–$95
- **+$10 Narrows Bridge surcharge displayed prominently**
- Red warning box explaining bridge toll requirement
- Service info: Lockouts, Flat Tire, Jump Start, Fuel Delivery
- Call-to-action: (253) 322-5282
- Responsive mobile design
- Schema.org structured data for SEO

**Page template:** `/zip/[zipcode].html`

Examples:
- https://cascaderoadside.com/zip/98366.html (Port Orchard)
- https://cascaderoadside.com/zip/98310.html (Bremerton)

### 4. ✅ Interactive Service Area Map
**File:** `service-area-map.html`
**Live URL:** https://cascaderoadside.com/service-area-map.html

Features:
- **Leaflet.js mapping library** with OpenStreetMap tiles
- **GeoJSON zip code boundaries** from State-zip-code-GeoJson
- **Color-coded polygons:**
  - 🟠 Orange = Standard service areas (86 zips)
  - 🔴 Red = +$10 Bridge Surcharge areas (9 zips, Kitsap County)
- **Interactive popups** on click showing city, zip, and surcharge info
- **Hover effects** for better UX
- **Centered on Puyallup** (47.1854, -122.2929), zoom level 9
- **Responsive** for mobile devices
- **Header + CTA button** linked to call (253) 322-5282
- **Legend** explaining service areas

### 5. ✅ Live Deployment
- **Host:** Netlify
- **Production URL:** https://cascaderoadside.com
- **Deployment:** Success ✓
- **Build time:** 3.4 seconds

## Business Impact

### Revenue
- **9 new service zip codes** now available
- **+$10 bridge surcharge** = Additional $90/month per call (estimated 1 call/zip/month)
- **Visibility:** All zips have SEO-optimized landing pages

### Coverage
- Bremerton area (largest Kitsap city)
- Port Orchard (high-traffic corridor)
- Poulsbo, Silverdale, Gorst (secondary markets)
- **Service range:** ~45 min from Puyallup via Tacoma Narrows Bridge

### Marketing
- Service area map is intuitive and shareable
- Transparent pricing (bridge surcharge noted upfront)
- Zero customer surprises at checkout

## Files Modified/Created

**Modified:**
- `service-area-zipcodes.csv` — Added 9 Kitsap zips

**Created:**
- `zip/98366.html` (Port Orchard)
- `zip/98367.html` (Port Orchard)
- `zip/98310.html` (Bremerton)
- `zip/98311.html` (Bremerton)
- `zip/98312.html` (Bremerton)
- `zip/98314.html` (Bremerton)
- `zip/98337.html` (Gorst)
- `zip/98383.html` (Silverdale)
- `zip/98370.html` (Poulsbo)
- `service-area-map.html` — Interactive Leaflet map
- `create_kitsap_pages.py` — Script used to generate pages

## Test Links

- Main site: https://cascaderoadside.com
- Service area map: https://cascaderoadside.com/service-area-map.html
- Sample Kitsap zip page: https://cascaderoadside.com/zip/98366.html
- Call (253) 322-5282 for dispatch

---
**Status:** ✅ Complete. All systems live and deployed.
