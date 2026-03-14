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
