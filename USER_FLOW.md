# Service Request User Flow

## Customer Journey

### 1️⃣ Homepage Discovery
```
https://cascaderoadside.com
├─ See main CTA: "🎯 Request Service Now"
├─ or Click nav link: "🎯 Request Service"
└─ → Navigates to /service-area-map.html#request
```

### 2️⃣ Map Page - Location Detection
```
/service-area-map.html
├─ See map with 98 ZIP codes highlighted
├─ Click "📍 Find My Location" button
├─ Browser requests GPS permission
└─ Location acquired: Lat/Lng captured
```

### 3️⃣ Service Area Check
```
If location is in service area (Puget Sound):
├─ Button changes to: "✓ You are in our service area!"
├─ "🎯 Request Service" button appears (bottom-right)
├─ Address auto-filled via reverse geocoding
└─ Location info displayed in form

If location is OUTSIDE service area:
├─ Button changes to: "⚠ Outside service area"
├─ "🎯 Request Service" button hidden
└─ Form not available
```

### 4️⃣ Service Request Form Opens
```
Click "🎯 Request Service" →
├─ Panel slides in from right
├─ Shows form with fields:
│  ├─ Name * (required)
│  ├─ Phone * (required)
│  ├─ Address * (auto-filled, editable)
│  ├─ Service Type * (dropdown)
│  │  ├─ 🔓 Lockout - $95
│  │  ├─ 🛞 Flat Tire - $95
│  │  ├─ 🔋 Jump Start - $85
│  │  └─ ⛽ Fuel Delivery - $95
│  ├─ Additional Notes (optional textarea)
│  └─ "Send Request — We'll Call You Back" button
└─ Narrows bridge surcharge warning (if applicable)
```

### 5️⃣ Form Submission
```
User fills form and clicks "Send Request"
├─ Form validation (required fields checked)
├─ Button shows: "<spinner> Sending..."
├─ POST to /.netlify/functions/service-request
│  ├─ Body includes:
│  │  ├─ name
│  │  ├─ phone
│  │  ├─ address
│  │  ├─ lat/lng (from GPS)
│  │  ├─ service_type
│  │  ├─ notes
│  │  └─ zone (Standard or Narrows)
│  └─ Function processes request
└─ Awaiting response
```

### 6️⃣ Alert Sent to Doug
```
Serverless Function (/service-request):
├─ Receives POST request ✓
├─ Validates data
├─ Sends SMS to (253) 412-3485 via Twilio:
│  └─ "🚨 NEW SERVICE REQUEST
│     Name: John Smith
│     Phone: (555) 123-4567
│     Service: Lockout
│     Location: 123 Main St, Puyallup, WA 98371
│     Zone: Standard
│     Notes: Keys locked in car
│     Call them back NOW!"
├─ Initiates voice call to (253) 412-3485
│  └─ TwiML response: "You have a new roadside 
│     service request from John Smith needing Lockout.
│     Call them back at (555) 123-4567 immediately."
└─ Returns success JSON
```

### 7️⃣ Customer Confirmation
```
Form submission completed:
├─ Green confirmation message appears:
│  └─ "✅ Request sent! Doug will call you back within 5 minutes."
├─ Form hides temporarily
├─ After 5 seconds:
│  ├─ Form resets
│  ├─ Confirmation message fades
│  └─ Panel closes (optional)
└─ Customer awaits call from Doug
```

---

## Backend Flow Diagram

```
┌─────────────────────────┐
│   Customer Browser      │
│  (service-area-map.html)│
└────────────┬────────────┘
             │
    [Form Submit] → POST /.netlify/functions/service-request
             │
             ↓
┌─────────────────────────────────────────────┐
│      Netlify Serverless Function            │
│   (netlify/functions/service-request.js)    │
└────────────┬────────────────────────────────┘
             │
             ├─→ Parse request body
             │
             ├─→ Validate fields
             │
             ├─→ Initialize Twilio client
             │
             ├─→ Format phone numbers (E.164)
             │
             ├─→ Build SMS message
             │   └─→ (253) 412-3485 via Twilio API
             │
             ├─→ Get TwiML URL
             │   └─→ /.netlify/functions/twiml?name=X&phone=Y&service=Z
             │
             ├─→ Initiate voice call
             │   └─→ (253) 412-3485 with TwiML
             │
             └─→ Return success JSON
                 {
                   "success": true,
                   "message": "...",
                   "requestId": "SMS_SID",
                   "callSid": "CALL_SID",
                   "customerPhone": "...",
                   "timestamp": "..."
                 }
             
             ↓
┌─────────────────────────┐
│   Twilio Servers        │
├─────────────────────────┤
│ 1. SMS Message Sent ✓   │
│ 2. Voice Call Initated  │
│    (calls function)     │
└────────────┬────────────┘
             │
             ↓
┌──────────────────────────────────────┐
│    TwiML Function Response           │
│  (netlify/functions/twiml.js)        │
│                                      │
│  <Say>You have a new roadside        │
│  service request from [Name]         │
│  needing [Service].                  │
│  Call them back at [Phone]           │
│  immediately.</Say>                  │
└──────────────────────────────────────┘
             │
             ↓
┌─────────────────────────┐
│   Doug's Phone          │
│  📱 ☎️ INCOMING CALL     │
│  📨 NEW SMS MESSAGE     │
└─────────────────────────┘
```

---

## Error Handling

### Missing Required Fields
```json
{
  "statusCode": 400,
  "error": "Missing required fields: name, phone, service_type"
}
```

### Twilio API Error
```json
{
  "statusCode": 500,
  "success": false,
  "error": "Failed to send SMS: [Twilio error message]"
}
```

### Network Timeout
```
Customer sees: "Error sending request: timeout"
Form remains open for retry
```

---

## Success Metrics

✅ **Customer receives confirmation** - 100% (instant)
✅ **Doug receives SMS** - SMS sent successfully
✅ **Doug receives voice call** - Call initiated (may not connect if phone off)
✅ **Call back in 5 minutes** - Depends on Doug's availability
✅ **Service completion** - Depends on technician dispatch

---

## Mobile Responsive Design

### Desktop (>600px)
- Service form panel slides in from right (380px wide)
- Full map visible
- Request button in bottom-right

### Mobile (<600px)
- Service form panel takes full width
- Map still visible behind (scrollable)
- Request button adjusted for small screens
- Touch-friendly buttons and inputs

---

**Last Updated:** 2026-07-14
**Status:** Production Ready ✅
