# Cascade Roadside AI Phone Answering System

A complete Python/Flask solution for receiving and processing roadside assistance calls automatically using Twilio and AI voice responses.

## Features

✅ **AI Voice IVR** - Professional voice greetings and prompts using Twilio's voice synthesis  
✅ **Multi-step Call Flow** - Collects caller name, location, service type, and callback number  
✅ **SMS Job Dispatch** - Sends formatted job requests to dispatcher (Doug)  
✅ **Customer Confirmation** - Automatic SMS confirmation with ETA  
✅ **Call Logging** - Tracks all incoming calls and data collection  
✅ **Production Ready** - Flask app with Twilio webhooks and error handling  

## System Architecture

```
Incoming Call → Twilio → Flask /incoming-call endpoint
    ↓
IVR Flow: Collect Name → Location → Service Type → Callback Number
    ↓
Process Request → Send SMS to Doug → Send Confirmation to Customer
    ↓
End Call
```

## Prerequisites

- Python 3.11 or higher
- Twilio account with active phone number (253) 322-5282
- Access to receive SMS on dispatcher phone (253) 412-3485
- Flask and Twilio Python SDK

## Installation

### 1. Install Dependencies

```bash
/opt/homebrew/bin/python3.11 -m pip install -r requirements.txt
```

Or if pip3.11 is aliased:

```bash
pip3.11 install flask twilio python-dotenv requests
```

### 2. Verify Imports

```bash
/opt/homebrew/bin/python3.11 -c "
from flask import Flask
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse
print('✓ All imports successful!')
"
```

## Configuration

All credentials are hardcoded in `app.py` for this deployment:

- **TWILIO_ACCOUNT_SID**: `ACb73bfa7b6b412acb981adbe42542de35`
- **TWILIO_AUTH_TOKEN**: `11e16ef185238e23d40523f28d9ff5f7`
- **TWILIO_PHONE**: `(253) 322-5282` (your business number)
- **DOUG_PHONE**: `(253) 412-3485` (dispatcher SMS recipient)

### For Production Deployment

Move credentials to environment variables:

```bash
export TWILIO_ACCOUNT_SID="your_sid_here"
export TWILIO_AUTH_TOKEN="your_token_here"
```

Then update `app.py`:

```python
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
```

## Usage

### Local Development

```bash
cd /Users/dougwinker/.openclaw/workspace/cascade-roadside
/opt/homebrew/bin/python3.11 app.py
```

Server runs on `http://localhost:5000`

Output:
```
[✓] Cascade Roadside AI System starting...
[✓] Twilio Account SID: ACb73bfa7b6b412acb981adbe42542de35
[✓] Business Phone: (253) 322-5282
[✓] Doug's Phone: (253) 412-3485

Available endpoints:
  POST /incoming-call - Twilio webhook for incoming calls
  POST /process-request - Process completed job request
  POST /webhook-status - Call status updates
  GET / - Health check

[💾] Running on http://localhost:5000
[⚠️]  For production, use Gunicorn or similar WSGI server
```

### Production Deployment

For production, use a WSGI server like Gunicorn:

```bash
pip3.11 install gunicorn
cd /Users/dougwinker/.openclaw/workspace/cascade-roadside
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## Twilio Configuration

### 1. Configure Incoming Call Webhook

In your Twilio Console:

1. Go to **Phone Numbers** → **(253) 322-5282**
2. Under **Voice & Fax**:
   - **Configure With**: Webhooks
   - **A Call Comes In**: Set to your Flask server URL + `/incoming-call`
   - Example: `https://your-domain.com/incoming-call`

### 2. Configure Call Status Webhook

1. Same phone number settings
2. Under **Webhooks**:
   - **Status Callbacks**: Point to `/webhook-status`
   - Example: `https://your-domain.com/webhook-status`

### 3. Expose Local Server to Twilio

For local development, use **ngrok**:

```bash
ngrok http 5000
```

Then use the ngrok URL in Twilio settings:
- `https://abc123.ngrok.io/incoming-call`

## Call Flow Details

### Step 1: Greeting
**System**: "Thank you for calling Cascade Roadside! I'm here to help get you back on the road. What is your name?"
**Caller**: Speaks their name

### Step 2: Location
**System**: "Got it, [Name]. What is your current location or address?"
**Caller**: Speaks their address/location

### Step 3: Service Type
**System**: "What service do you need? For example: lockout, flat tire, fuel delivery, or jump start?"
**Caller**: Speaks service needed

### Step 4: Callback Number
**System**: "What's the best callback number for you?"
**Caller**: Speaks their phone number

### Step 5: Job Dispatch
**Backend**:
- Sends SMS to Doug (dispatcher): "🚨 NEW JOB REQUEST..."
- Sends SMS to customer: "Thanks [Name]! Cascade Roadside is on the way..."

### Step 6: Confirmation
**System**: "Perfect! We've received your request and will have someone on the way within 45 minutes. You'll receive a confirmation text shortly. Is there anything else?"
**Caller**: Responds with yes/no

### Step 7: Hangup
**System**: "Thank you for calling Cascade Roadside. We'll see you soon!"

## API Endpoints

### `GET /`
Health check endpoint.

**Response**: `Cascade Roadside AI System is running ✓`

---

### `POST /incoming-call`
Receives incoming calls from Twilio and starts the IVR flow.

**Twilio Parameters**:
- `From`: Caller's phone number
- `CallSid`: Unique call identifier
- `To`: Your business number

**Returns**: TwiML greeting and initial voice prompt

---

### `POST /process-request`
Processes the completed job request after all information is collected.

**Actions**:
1. Stores all customer information
2. Sends SMS to dispatcher (Doug)
3. Sends confirmation SMS to customer
4. Continues with final prompts

**SMS to Doug Format**:
```
🚨 NEW JOB REQUEST
Name: [Customer Name]
Location: [Address/Location]
Service: [Service Type]
Callback: [Phone Number]
Reply YES to accept or NO to decline
```

**SMS to Customer Format**:
```
Thanks [Name]! Cascade Roadside is on the way. 
ETA: 45 min or less. Questions? Call (253) 322-5282
```

---

### `POST /webhook-status`
Receives call status updates (completed, failed, busy, etc.)

**Twilio Parameters**:
- `CallSid`: Unique call identifier
- `CallStatus`: Status of the call
- `From`: Caller's phone number

**Returns**: HTTP 200 OK (no response body needed)

---

## Troubleshooting

### "ModuleNotFoundError: No module named 'flask'"
Install dependencies:
```bash
pip3.11 install flask twilio
```

### "Twilio credentials not configured"
Check that `TWILIO_ACCOUNT_SID` and `TWILIO_AUTH_TOKEN` are set in `app.py`

### "Failed to send SMS to Doug"
- Verify phone number `(253) 412-3485` is correct
- Check Twilio account balance
- Ensure `TWILIO_PHONE` is verified in Twilio console
- Check SMS logs in Twilio dashboard

### Caller doesn't hear voice prompts
- Verify TwiML response format is correct
- Check Twilio console for call logs
- Test with a different phone number
- Ensure Flask app is running and responding to webhooks

### SMS arrives but with wrong information
- Check speech recognition accuracy in Twilio logs
- May need to add grammar hints for better recognition
- Consider adding confirmation prompts: "I heard [X], is that correct?"

## Development & Testing

### Test the Health Check

```bash
curl http://localhost:5000/
```

Expected: `Cascade Roadside AI System is running ✓`

### Simulate an Incoming Call

```bash
curl -X POST http://localhost:5000/incoming-call \
  -d "From=%2B12534125282&CallSid=CA1234567890abcdef&To=%2B12533225282"
```

### View Call Data

The `call_data` dictionary in memory stores current active calls:

```python
# In app.py, you can log:
print(call_data)
```

### Database Integration (Future)

For production, replace the `call_data` dictionary with a database:

```python
# Example with SQLite
import sqlite3

def save_call_data(call_sid, name, location, service, callback):
    conn = sqlite3.connect('cascade_roadside.db')
    c = conn.cursor()
    c.execute("""
        INSERT INTO jobs (call_sid, name, location, service, callback, created_at)
        VALUES (?, ?, ?, ?, ?, datetime('now'))
    """, (call_sid, name, location, service, callback))
    conn.commit()
    conn.close()
```

## Files

- **app.py** - Main Flask application with all endpoints and call flow logic
- **requirements.txt** - Python package dependencies
- **README.md** - This file, with setup and deployment instructions

## License

Proprietary - Cascade Roadside

## Support

For issues or questions about this system, contact the development team.

---

**Last Updated**: June 29, 2026  
**Version**: 1.0  
**Status**: Production Ready ✓
