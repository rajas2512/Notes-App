#import website package and grab the create_app function 
# and use that to create an application and run it
#website->python package, __init__.py becomes a python package
from website import create_app 

app = create_app()

if __name__ == '__main__': #only if we run main.py and not import main.py are we going to execute this line
    app.run(debug=True) #Run our flask application, debug = true indicates if we make any change in our python code its gng to automatically rerun the web server
    
