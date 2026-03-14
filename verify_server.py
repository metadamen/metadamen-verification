import os
from flask import Flask, request, render_template
import json


app = Flask(__name__)

# Example certificate database
certs = {
    "1000132": "Khushi Kumari",
    "1000133": "Aakriti",
    "1000134": "Anjali Raj",
    "1000135": "Shobha Kumari"
}
with open("cert_counter.json") as f:
    certs = json.load(f)

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
    port = int(os.environ.get("PORT", 5050))
    app.run(host="0.0.0.0", port=port)
