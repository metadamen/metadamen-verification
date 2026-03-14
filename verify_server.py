from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

with open("cert_counter.json") as f:
    certs = json.load(f)

@app.route("/verify")
def verify():

    cert = request.args.get("cert")
    valid = cert in certs

    if request.headers.get("Accept") == "application/json":
        return jsonify({
            "cert": cert,
            "valid": valid,
            "issued_by": "Metadamen Pvt Ltd"
        })

    return render_template(
        "verify.html",
        cert=cert,
        valid=valid
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)