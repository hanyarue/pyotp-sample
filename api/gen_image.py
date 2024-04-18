import os
import pyqrcode
import io
import base64


class get_image:
    data = None
    
    def __init__(self, data):
        self.data = data
    
    def create_qr(self):
        print(f'QR Data::{self.data}')
        c = pyqrcode.create(self.data)
        s = io.BytesIO()
        
        c.png(s,scale=6)
        encoded = base64.b64encode(s.getvalue()).decode("ascii")
        tag_img = '''<img src="data:image/png;base64,''' + encoded + '''">'''
        
        print(tag_img)   
        
        self.__save_html(val_tag=tag_img) 
        
    def __save_html(self, val_tag):
        with open("output.html", "w") as file:
            file.writelines(val_tag)
            
        print('Save HTML')
        