#!/usr/bin/env python

'''
Send an multipart email with HTML and plain text alternatives. The message
should be constructed as a plain-text file of the following format:
    
    From: Your Name <your@email.com>
    To: Recipient One <recipient@to.com>
    Subject: Your subject line
    ---
    Markdown content here

@copyright https://gist.github.com/cleverdevil/8250082

The script accepts content from stdin and, by default, prints the raw
generated email content to stdout.

Preview your message on OS X by invoking the script with `-p` or 
`--preview`, and it will open in your default mail client.

'''


import os
import sys
import json
import argparse
import smtplib
import subprocess
import datetime, locale
import base64

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

try:
    import pygments
    import markdown as markdown
except ImportError:
    print('This script requires pygements and markdown to be installed.')
    print('Please:')
    print('   pip install pygments markdown')
    sys.exit(0)

# define arguments
parser = argparse.ArgumentParser(description='Format and send markdown-based emails.',
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog=__doc__)
parser.add_argument('-p', '--preview', action='store_true', 
                    help='Preview the email in Apple Mail.')
args = parser.parse_args()

# read in raw message content
content = sys.stdin.read()

# render the markdown into HTML 
css = subprocess.check_output(['pygmentize', '-S', 'colorful', '-a', '.codehilite', '-f', 'html'])
css = css.decode("utf-8")

content = content.strip()
html_content = '<style type="text/css">'+css+'</style>'

with open("three-balls.png", "rb") as image_file:
    encoded_string = (base64.b64encode(image_file.read())).decode("utf-8")

#html_content += '<table width=80%><tr><td>'
html_content += '<center><img align="center" src="data:image/png;base64,'+encoded_string+'" />'
html_content += '</center>'
html_content += markdown.markdown(content, extensions=['extra', 'codehilite', 'pymdownx.superfences'])
#html_content += '</td><tr></table>'

# create a multipart email message
message = MIMEMultipart('alternative')

# set the headers
message['To'] = "julia@services.cnrs.fr"
message['From'] = "pierre.navaro@univ-rennes1.fr"

today = datetime.datetime.now()
locale.setlocale(locale.LC_ALL, 'fr_FR')
month = today.strftime("%B")
year = today.strftime("%Y")
message['Subject'] = f"Nouvelles Julia {month} {year}"

message.attach(MIMEText(content, 'plain'))
message.attach(MIMEText(html_content, 'html'))

if args.preview:
    open('/tmp/preview.eml', 'w').write(message.as_string())
    os.system('open -a Mail /tmp/preview.eml')
else:
    print(message.as_string())
