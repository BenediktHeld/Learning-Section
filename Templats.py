import os

#Import Flask Class
from flask import Flask,render_template

#Create application Object
app = Flask(__name__)

#Connect to an HTML FILE
@app.route('/')
def index(): 
    #Create a folder 'templates' in the same folder like main.py 
    #and import 'render_template' then return render_template(HTML_FILE_NAME)
    return render_template('basic.html')

'''
    - The syntax for Control Flow:  {%for ...%}
'''
@app.route('/Template_Variables')
def Template_Variables(): 
        UserLogin = True
        List = ["Bene","Jonas","Miriam"]
        return render_template('basic.html',List=List,UserLogin=UserLogin)

'''  So kann man die Variable in HTML aufrufen:
        <ul>
            #For Loop
            {%for x in List%}
            <li>{{x}}</li>
            {%endfor%}
        </ul>

            #If Loop 
         {% if UserLogin %}
             <p>You are logged in</p>
        {% else %}
            <p>Login</p>
        {% endif %}
'''


if __name__ == '__main__':
    app.run(debug=True)
