from swagger_server.resources.db import db


class Streaming_Device(db.Model):
    __tablename__ = "streaming_devices"
    id_streaming_device= db.Column(db.Integer, primary_key=True)
    name_streaming_device= db.Column(db.String(50))
    state_streaming_device= db.Column(db.Boolean)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    

    def __init__(self, payload):
        self.name_streaming_device = payload.get('name_streaming_device')
        self.state_streaming_device = payload.get('state_streaming_device')
        self.created_at = payload.get('created_at')
        

    def to_json(self):
        return {
            "id_streaming_device":self.id_streaming_device, 
            "name_streaming_device":self.name_streaming_device, 
            "state_streaming_device":self.state_streaming_device, 
            "created_at":self.created_at, 
            
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def destroy(self):
        db.session.delete(self)
        db.session.commit()
