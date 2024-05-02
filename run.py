from app import app, db

"""
!!! NOTICE
>>> from app.app import db
>>> db.create_all()
>>> exit()
"""

if __name__=='__main__':
    app.run()
    db.create_all()
