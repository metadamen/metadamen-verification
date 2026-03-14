from flask import Flask, request, render_template

app = Flask(__name__)

# Example certificate database
certs = {
    "CERT001": "Rahul Sharma",
    "CERT002": "Priya Singh"
}

@app.route("/verify")
def verify():

    cert = request.args.get("cert")

    valid = cert in certs

    student = certs.get(cert)

    return render_template(
        "verify.html",
        cert=cert,
        valid=valid,
        student=student
    )

if __name__ == "__main__":
    app.run(debug=True)
