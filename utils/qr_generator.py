import qrcode

def generate_qr(session_id):

    url = f"http://localhost:8502/?session={session_id}"

    img = qrcode.make(url)

    img.save(
        f"session_{session_id}.png"
    )

    return f"session_{session_id}.png"