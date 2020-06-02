Refactoring

export FLASK_DEBUG=0

py -m pip install -r requirements.txt

py -m flask db init
py -m flask db migrate
py -m flask db upgrade

py -m flask run

app/
    errors/                             <-- blueprint package
        __init__.py                     <-- blueprint creation
        handlers.py                     <-- error handlers
    templates/
        errors/                         <-- error templates
            404.html
            500.html
    __init__.py                         <-- blueprint registration


app/
    auth/                               <-- blueprint package
        __init__.py                     <-- blueprint creation
        email.py                        <-- authentication emails
        forms.py                        <-- authentication forms
        routes.py                       <-- authentication routes
    templates/
        auth/                           <-- blueprint templates
            login.html
            register.html
            reset_password_request.html
            reset_password.html
    __init__.py                         <-- blueprint registration