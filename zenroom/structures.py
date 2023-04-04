from datetime import datetime
from zenroom import db
from datetime import datetime
from dateutil import parser

date = datetime.utcnow()
dt = date.strftime('%d/%m/%Y %H:%M:%S')


print(dt)

class Diarydb(db.Model):
    userid = db.Column(db.Integer, autoincrement=True,primary_key=True)
    title = db.Column(db.Text, nullable=False)
    date = db.Column(db.Text, nullable=False, default=dt)
    text = db.Column(db.Text, nullable=False)
    user =  db.Column(db.String(20), nullable=False, default="test_user")
    def __repr__(self):
        return f"Diarydb(title='{self.title}', text='{self.text}', user='{self.user}')"
