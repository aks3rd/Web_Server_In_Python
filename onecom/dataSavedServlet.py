from urllib.parse import urlparse,parse_qs
from html.parser import HTMLParser
from html.entities import name2codepoint
#from mysql.connector import MySQLConnection, Error
#from python_mysql_dbconfig import read_db_config
import os
def insert(name,cityCode):
    query = "INSERT INTO members(name,cityCode) " \
            "VALUES(%s,%s)"
    args = (name, cityCode)
 
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
 
        cursor = conn.cursor()
        cursor.execute(query, args)
 
        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')
 
        conn.commit()
    except Error as error:
        print(error)
 
    finally:
        cursor.close()
        conn.close()

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)
        for attr in attrs:
            print("     attr:", attr)

    def handle_endtag(self, tag):
        print("End tag  :", tag)

    def handle_data(self, data):
        print("Data     :", data)

    def handle_comment(self, data):
        print("Comment  :", data)

    def handle_entityref(self, name):
        c = chr(name2codepoint[name])
        print("Named ent:", c)

    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print("Num ent  :", c)

    def handle_decl(self, data):
        print("Decl     :", data)

class RequestHandler:
 def __init__(self):
  pass
 
 def getResponse(self,baseHttpRequestHandler):
  print("Request Arrived")
  parsed=urlparse(baseHttpRequestHandler.path)
  query=parse_qs(parsed.query)
  name=query.get('nm')[0]
  gender=query.get("gdr")[0]
  if query.get("adlt")==None:
   adult=None
  else:
   adult=query.get("adlt")[0]
  address=query.get("ad")[0]
  city=query.get("ct")[0]
  print("Name is : %s"%name)
  print("Gender is : %s"%gender)
  print("Adult Status : %s"%adult)
  print("Address : %s"%address)
  print("City : %s"%city)
  #insert(name,int(city))
  fname="test.html"
  html=open(fname,"w")
  html.write("""<!doctype html><html><head>""")
  html.write("""<title>Response From Python Server</title></head>""")
  html.write("""<body><h1>Data Saved</h1><a href='/onecom/index.html'><button>Ok</button>""")
  html.write("""</body></html>""")
  html.close()
  html=open(fname,"rb")
  baseHttpRequestHandler.send_response(200)
  baseHttpRequestHandler.send_header("Content-type","text/html")
  baseHttpRequestHandler.end_headers()
  baseHttpRequestHandler.wfile.write(html.read())
  html.close()
  os.remove(fname)
