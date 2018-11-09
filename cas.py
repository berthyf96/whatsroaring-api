import sys, os, cgi, urllib.parse, re
from requests.utils import requote_uri
form = cgi.FieldStorage()

class CASClient:
   def __init__(self):
      self.cas_url = 'https://fed.princeton.edu/cas/'
   def Authenticate(self):
      #If the request contains a login ticket, try to validate it
      print(form)
      if 'ticket' in form:
         netid = self.Validate(form['ticket'].value)
         if netid != None:
            return netid
      # No valid ticket; redirect the browser to the login page to get one
      login_url = self.cas_url + 'login' \
         + '?service=' + urllib.parse.quote(self.ServiceURL())
      print('Location: ' + login_url)
      print('Status-line: HTTP/1.1 307 Temporary Redirect')
      print("")
      sys.exit(0)
   def Validate(self, ticket):
      val_url = self.cas_url + "validate" + \
         '?service=' + urllib.quote(self.ServiceURL()) + \
         '&ticket=' + urllib.quote(ticket)
      r = urllib.urlopen(val_url).readlines()   # returns 2 lines
      if len(r) == 2 and re.match("yes", r[0]) != None:
         return r[1].strip()
      return None
   def ServiceURL(self):
      print('service')
      print(os.environ)
      if 'REQUEST_URI' in os.environ:
         ret = 'http://' + os.environ['HTTP_HOST'] + os.environ['REQUEST_URI']
         ret = re.sub(r'ticket=[^&]*&?', '', ret)
         ret = re.sub(r'\?&?$|&$', '', ret)
         return ret
         #$url = preg_replace('/ticket=[^&]*&?/', '', $url);
         #return preg_replace('/?&?$|&$/', '', $url);
      return "something is badly wrong"
 
def main():
  print("CASClient does not run standalone")
if __name__ == '__main__':
  main()