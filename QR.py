import qrcode
import os
import urllib.parse

def create_html_page(text, filename="message.html"):
    """Create an HTML page with popup effect for the text"""
    
    # Escape the text for safe HTML display
    safe_text = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace("'", '&#39;')
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Secret Message</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }}
        
        .popup-container {{
            background: white;
            border-radius: 20px;
            padding: 40px 30px;
            max-width: 500px;
            width: 100%;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            opacity: 0;
            transform: scale(0.9);
            animation: popIn 0.4s ease-out forwards;
        }}
        
        @keyframes popIn {{
            to {{
                opacity: 1;
                transform: scale(1);
            }}
        }}
        
        .icon {{
            text-align: center;
            font-size: 50px;
            margin-bottom: 20px;
        }}
        
        h1 {{
            text-align: center;
            color: #333;
            font-size: 24px;
            margin-bottom: 20px;
        }}
        
        .message {{
            background: #f7f7f7;
            border-radius: 12px;
            padding: 25px;
            color: #333;
            font-size: 18px;
            line-height: 1.6;
            text-align: center;
            word-wrap: break-word;
        }}
        
        .footer {{
            text-align: center;
            margin-top: 20px;
            color: #666;
            font-size: 14px;
        }}
    </style>
</head>
<body>
    <div class="popup-container">
        <div class="icon">📱</div>
        <h1>Your Message</h1>
        <div class="message">
            {safe_text}
        </div>
        <div class="footer">
            Scanned successfully ✓
        </div>
    </div>
</body>
</html>"""
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    return os.path.abspath(filename)

def generate_qr_with_popup():
    """
    Generate a QR code that opens a webpage with popup effect.
    """
    
    print("=" * 60)
    print("QR CODE GENERATOR WITH POPUP EFFECT")
    print("=" * 60)
    
    # Get text input from user
    print("\nEnter the text for your popup message:")
    text = input("> ")
    
    if not text.strip():
        print("Error: Text cannot be empty!")
        return
    
    # Get QR code filename
    print("\nEnter QR code filename (press Enter for 'qr_code.png'):")
    qr_filename = input("> ").strip()
    
    if not qr_filename:
        qr_filename = "qr_code.png"
    elif not qr_filename.endswith('.png'):
        qr_filename += '.png'
    
    # Create HTML file
    html_filename = "message.html"
    html_path = create_html_page(text, html_filename)
    
    print(f"\n✓ HTML page created: {html_filename}")
    
    # Create file URL for the QR code
    file_url = f"file:///{html_path.replace(os.sep, '/')}"
    
    # Create QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    
    qr.add_data(file_url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(qr_filename)
    
    print(f"✓ QR code created: {qr_filename}")
    
    print("\n" + "=" * 60)
    print("SUCCESS! 🎉")
    print("=" * 60)
    print("\n📱 INSTRUCTIONS:")
    print("-" * 60)
    print("OPTION 1 - Local Testing (same device):")
    print(f"  1. Open '{html_filename}' in your browser")
    print("  2. You'll see the popup effect")
    print()
    print("OPTION 2 - For phone scanning (RECOMMENDED):")
    print("  You need to host the HTML file online.")
    print("  Free hosting options:")
    print("    • GitHub Pages (github.com)")
    print("    • Netlify Drop (app.netlify.com/drop)")
    print("    • Vercel (vercel.com)")
    print()
    print("  Steps:")
    print(f"  1. Upload '{html_filename}' to any free hosting")
    print("  2. Get the public URL (e.g., https://yoursite.netlify.app)")
    print("  3. Run this script again and enter the URL when asked")
    print("=" * 60)
    
    # Ask if user wants to create QR with custom URL
    print("\n\nDo you have a URL to create QR code? (y/n):")
    choice = input("> ").strip().lower()
    
    if choice == 'y' or choice == 'yes':
        print("\nEnter the full URL (e.g., https://yoursite.com/message.html):")
        url = input("> ").strip()
        
        if url:
            print("\nEnter QR code filename:")
            new_qr_filename = input("> ").strip() or "qr_code_url.png"
            if not new_qr_filename.endswith('.png'):
                new_qr_filename += '.png'
            
            qr2 = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,
            )
            qr2.add_data(url)
            qr2.make(fit=True)
            img2 = qr2.make_image(fill_color="black", back_color="white")
            img2.save(new_qr_filename)
            
            print(f"\n✓ QR code with URL created: {new_qr_filename}")
            print("✓ Scan this QR code with your phone to see the popup!")
    
    # Ask if user wants to create another
    print("\n\nCreate another QR code? (y/n):")
    choice = input("> ").strip().lower()
    
    if choice == 'y' or choice == 'yes':
        print("\n")
        generate_qr_with_popup()

if __name__ == "__main__":
    try:
        generate_qr_with_popup()
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")