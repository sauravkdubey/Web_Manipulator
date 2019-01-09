#############################################################################################################################################
####################################################----------------------------------------##################################################

#--------------------------------------------------     AUTHOR - SAURAV KUMAR DUBEY        ---------------------------------------------#
#--------------------------------------------------     Date - 30/12/2018                  ---------------------------------------------#



from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def homepage():
    return render_template("index.html")

#------------------------------------------------------------------ STARTS BROWSER -------------------------------------------------------#

@app.route('/start', methods=['GET'])
def start():				
				
    if 'browser' in request.args and 'url' in request.args:
    
        print "fegerge"
        browser_name = str(request.args['browser'])
        url = str(request.args['url'])
        print browser_name
        print url
        
        if browser_name == "chrome":
            import webbrowser
            chrome_path = '/usr/bin/google-chrome %s'
            webbrowser.get(chrome_path).open(url)                 # get url
            return "Chrome fired up with specified url"
            
        elif browser_name == "mozilla":
            import webbrowser
            mozilla_path = '/usr/bin/firefox %s'
            webbrowser.get(mozilla_path).open(url)                # get url
            return "Mozilla fired up with specified url"
            
        else:
            return "This browser isnt available"
            
            
    elif 'browser' in request.args:
        browser_name = str(request.args['browser'])
        
        if browser_name == "chrome":
            import webbrowser
            chrome_path = '/usr/bin/google-chrome %s'
            webbrowser.get(chrome_path).open("https://www.google.com")
            return "Chrome fired up"
            
        elif browser_name == "mozilla":
            import webbrowser
            mozilla_path = '/usr/bin/firefox %s'
            webbrowser.get(mozilla_path).open("https://www.google.com")
            return "Mozilla fired up "
            
        else:
            return "This browser isnt available"
            
    elif 'url' in request.args:
        return "Error only url provided"

#------------------------------------------------------------- STOPS BROWESER ---------------------------------------------------------------#

@app.route('/stop', methods=['GET'])

def stop():				
			
    if 'browser' in request.args:
    
        browser_name = str(request.args['browser'])
        print browser_name
        
        if browser_name == "chrome":
            import os
            browserExe = "chrome"
            os.system("pkill " + browserExe)
            return "CHROME CLOSED"
            
        elif browser_name == "mozilla":
            import os
            os.system("pkill " + "firefox")
            return "MOZILLA CLOSED"
            
        else:
            return "This browser isnt available"
            
    else:
        return "Browser name required"

##-------------------------------------------------------- DELETE ALL BROWSING SESSIONS ----------------------------------------------------##

@app.route('/cleanup', methods=['GET'])

def cleanup():

    if 'browser' in request.args:
        browser_name = str(request.args['browser'])
        print browser_name
        
        if browser_name == "chrome":
            # Successfully DELETS chrome content
            import os
            os.system("rm -rf ~/.cache/google-chrome/Default/Cache")
            os.system("rm -rf ~/.cache/google-chrome/Default/")
            os.system("rm -rf ~/.config/google-chrome/")
            os.system("rm -rf ~/.config/google-chrome/Default")
            return "Chrome Data IS CLEARED"
            
        elif browser_name == "mozilla":
            # Successfully DELETS mozilla content
            import os
            os.system("rm -rf ~/.cache/mozilla/")
            os.system("rm -rf ~/.mozilla/")
            return "Mozilla Data IS CLEARED"
            
    else:
        return "No query passed for filtration"

#-------------------------------------------------------------------------------------------------------------------------------------------##

if __name__ == '__main__':
    app.run(debug=True, port=8000)
    
    
    
    
    
    
    
#------------------------------------------------------------ END ---------------------------------------------------------------------###    
    
    
    
    
    
    
    
    
    
   
