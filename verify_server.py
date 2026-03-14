import os
from flask import Flask, request, render_template
import json

with open("cert_counter.json") as f:
    certs = json.load(f)

app = Flask(__name__)

# Example certificate database
certs = {
    "1000130": "Khushi Kumari",
    "1000131": "Aakriti",
    "1000132": "Anjali Raj",
    "1000133": "Shobha Kumari"
}

@app.route("/verify")
def verify():
    cert = request.args.get("cert")
    student = certs.get(cert)
    valid = student is not None

    return render_template(
        "verify.html",
        cert=cert,
        valid=valid,
        student=student
    )

if __name__ == "__main__":
    # Bind to the Render port
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
