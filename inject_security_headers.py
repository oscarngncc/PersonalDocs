import os

def inject_meta_headers(directory):
    headers = [
        '<meta http-equiv="X-Content-Type-Options" content="nosniff">',
        '<meta name="referrer" content="strict-origin-when-cross-origin">',
        '<meta name="permissions-policy" content="geolocation=(), midi=(), sync-xhr=(), microphone=(), camera=(), magnetometer=(), gyroscope=(), fullscreen=(), payment=()">',
        '<meta http-equiv="Content-Security-Policy" content="default-src \'self\'; script-src \'self\' \'unsafe-inline\' https://polyfill.io https://cdn.jsdelivr.net https://unpkg.com; style-src \'self\' \'unsafe-inline\'; frame-ancestors \'none\';">',
    ]

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                if headers[0] in content:
                    print(f"Headers already exist in {filepath}, skipping.")
                    continue

                # Find the end of the <head> tag and insert the headers
                head_end_index = content.find("</head>")
                if head_end_index != -1:
                    new_content = content[:head_end_index] + "\n" + "\n".join(headers) + "\n" + content[head_end_index:]
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Added headers to {filepath}")

if __name__ == "__main__":
    inject_meta_headers("site")
