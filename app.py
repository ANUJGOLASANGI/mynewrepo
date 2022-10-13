'''
flask is an web appln frame work used to control components  like front end ,backend and database

we can use flask to dvelop the machine learning  projects


pip install Flask    in cmd


whoisdomaintools
netcraft
shadon.io
# '''

# # from flask import Flask

# # #initilise the app

# # app=Flask(__name__)
# # #this will route to path

# # @app.route("/")

# # def home():
# #     return "hello, this is my home page"

# # if __name__=='__main__':   #this is always true
# #     app.run()





# # alternative way

# from flask import Flask
# app=Flask(__name__)
# @app.route("/")
# def hello():
#     return "hello anuj"

# if __name__=='__main__':
#     app.run()

  




#----------------------------------------------------------
from flask import Flask,redirect,url_for
app=Flask(__name__)
@app.route("/")
def home():
    return "this is my home page"
@app.route("/login")
def login():
    return "welcome anuj,you have succesfully logged in"
    


@app.route("/logout")
def logout():
    return redirect(url_for("home"))#this redirects back to home page
    #  return "logged  out successfully"
       


if __name__=='__main__':
    app.run()
