from Authentication_cont import app
from db import db

db.init_app(app)
@app.before_first_request
def create_table():
    db.create_all()
#if __name__ == '__main__':