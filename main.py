from flask import Flask,redirect,render_template
import flask
import os,random

try:
  import replitdb, requests
except: 
  os.system("pip3 install replitdb")
  import replitdb, requests
app = Flask('app')
db = replitdb.Client()
@app.route('/')
def home():
  return render_template('index.html', url=None)
@app.route("/Invalid")
def invalid():
  return redirect('/')
@app.route('/' ,methods=['POST'])
def adder():
  theurl = flask.request.form['url']
  valid=False
  customurl = flask.request.form['custom-name']
  
  characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9']
  urls=list(db.view('urls'))
  
  try: 
    requests.get(theurl)
    valid=True
  except:
    customurl = "Not Valid"
  while True:
    customized = True
    if valid:
      if customurl == "":
        customized = False
        for i in range(random.randint(1,6)):
          customurl+=random.choice(characters)
      if customurl not in urls:
        urls.append(customurl)
        db.set(urls=urls)
        db.set_dict({customurl:theurl})
        customurl="https://Url-Shortner.proryan.repl.co/"+customurl
        warning=""
        break
      else:
        customurl = ""
        if customized:
          warning = "Sorry your customized url was already taken"
  return render_template('index.html',url=customurl, warning=warning)
@app.route("/<page_name>")
def redirecting(page_name):
  url = db.view(page_name)
  print(url)
  if url != None: 
    return redirect(url)
  else:
     return redirect('/404')
app.run(host='0.0.0.0', port=8080, debug=True)