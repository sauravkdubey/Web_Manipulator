# Web_Manipulator

# About
Simple web service that allows one to interact with two web-browsers link, Google Chrome and Mozilla Firefox.

The interaction has four components

    **Start**: Starting a web-browser process with a given URL.
    **Stop**: Killing the web-browser process
    **Cleanup**: Delete all the browsing session information such as history, cache, cookies, downloads, saved passwords, etc.
    **Get URL**: Get the current active tab URL. 
 # Commands
 Commands in the form of restful URLs 
 
 ```bash
 
http:///start?browser=chrome&url=http://example.com should start Google Chrome and open http://example.com in the same. ( Similarly for Firefox)

http:///geturl?browser= should get the current active tab URL for the given browser

http:///stop?browser= should stop the given browser if it is running

http:///cleanup?browser= should clean up the browsing session for the given browser if has been stopped.
'''


