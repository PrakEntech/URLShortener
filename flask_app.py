
# A very simple Flask Hello World app for you to get started with...
import urllib,re
from flask import Flask, render_template, request, redirect
import random
app = Flask(__name__)

# Check https://regex101.com/r/A326u1/5 for reference
DOMAIN_FORMAT = re.compile(
    r"(?:^(\w{1,255}):(.{1,255})@|^)" # http basic authentication [optional]
    r"(?:(?:(?=\S{0,253}(?:$|:))" # check full domain length to be less than or equal to 253 (starting after http basic auth, stopping before port)
    r"((?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+" # check for at least one subdomain (maximum length per subdomain: 63 characters), dashes in between allowed
    r"(?:[a-z0-9]{1,63})))" # check for top level domain, no dashes allowed
    r"|localhost)" # accept also "localhost" only
    r"(:\d{1,5})?", # port [optional]
    re.IGNORECASE
)
SCHEME_FORMAT = re.compile(
    r"^(http|hxxp|ftp|fxp)s?$", # scheme: http(s) or ftp(s)
    re.IGNORECASE
)

def validate_url(url: str):
    url = url.strip()

    if not url:
        raise Exception("No URL specified")

    if len(url) > 2048:
        raise Exception("URL exceeds its maximum length of 2048 characters (given length={})".format(len(url)))

    result = urllib.parse.urlparse(url)
    scheme = result.scheme
    domain = result.netloc

    if not scheme:
        raise Exception("No URL scheme specified")

    if not re.fullmatch(SCHEME_FORMAT, scheme):
        raise Exception("URL scheme must either be http(s) or ftp(s) (given scheme={})".format(scheme))

    if not domain:
        raise Exception("No URL domain specified")

    if not re.fullmatch(DOMAIN_FORMAT, domain):
        raise Exception("URL domain malformed (domain={})".format(domain))

    return url

@app.route("/")
def input_data():
    return render_template('index.html')
@app.route("/<ur_l>")
def hello(ur_l):
    with open('data.bin','r')as f:
        a = f.read()
    a=a.split('\n')
    for i in range(len(a)):
        a[i] = a[i].split('|')
    a=a[:len(a)-1]
    for i in range(len(a)):
        for j in range(2):
            if ur_l == a[i][j]:
                if 'https://' not in a[i][j-1]:
                    x='https://'+a[i][j-1]
                    return redirect(x)
                if 'https://' in a[i][j-1]:return redirect(a[i][j-1])
@app.route("/",methods = ['POST'])
def getvalue():
    n = request.form['link']
    if 'https://' not in n:n='https://'+n
    try:
        validate_url(n)
        l=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M','-','_']
        with open('data.bin','r')as f:a=f.read()
        if n in a:
            a=a.split('\n')
            for i in range(len(a)):
                a[i] = a[i].split('|')
            a=a[:len(a)-1]
            for i in range(len(a)):
                if n in a[i]:break
            link = 'https://urlshortbyprakhar.pythonanywhere.com/'+a[i][1]
            return render_template('goto.html', name = link)
        else:
            with open('data.bin','a+')as f:
                f.write(n)
                f.seek(0)
                a=f.read()
            link_id=''
            while link_id in a:
                link_id=''
                for i in range(5):
                    link_id+=str(l[random.randint(0,len(l)-1)])
            link=link_id
            with open('data.bin','a')as f:
                f.write('|'+link)
                f.write('\n')
            link2 = 'https://urlshortbyprakhar.pythonanywhere.com/'+link
            return render_template('goto.html', name = link2)
    except: return 'NOT VALID URL'
if __name__=="__main__":
    app.run()

