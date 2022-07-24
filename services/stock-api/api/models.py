from app import db

class TwitterPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    msg = db.Column(db.String)
    created_at = db.Column(db.Date)
    def to_dict(self):
        return {
            "id": self.id,
            "msg": self.msg,
            "created_at": str(self.created_at.strftime('%d-%m-%Y'))
        }