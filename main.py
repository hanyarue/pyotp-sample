from api.gen_image import get_image
import pyotp
import time



class main:
    
    def __init__(self):        
        key = pyotp.random_base32()
        print(f'key==>{key}')
        
        totp = pyotp.TOTP(key)
        
        qrvalue = totp.provisioning_uri(name='alice@google.com', issuer_name='Secure App')
        
        print(qrvalue)
        
        self.gen_qrcode(qrvalue)

        
        
        val = totp.now() # => '492039'
        print(val)
        
        

        # # OTP verified for current time
        # totp.verify('492039') # => True
        # #time.sleep(30)
        # totp.verify('492039') # => False
    def gen_qrcode(self, data):
        image = get_image(data)
        image.create_qr()
        
        
        
        
if __name__ == "__main__":
    print("OTP Sample...")
    main()
    
        