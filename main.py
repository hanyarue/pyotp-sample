from api.db_handler import db_handler
from api.gen_image import get_image
import pyotp
import time



class main:
    
    def __init__(self):
        self.db = db_handler()
        self.json_data = self.db.data
   

        # # OTP verified for current time
        # totp.verify('492039') # => True
        # #time.sleep(30)
        # totp.verify('492039') # => False
    def task(self):
         
        self.json_data = self.db.data
        
        print(f"Load Data==>{ self.json_data}")
        while True:
            try:
                print('')
                print('========================================')
                print('작업을 선택하세요.')
                task_val = input('1: 신규등록 / 2: OTP 검증::')
                
                if(task_val == '1'):
                    print('신규 등록을 진행합니다.')
                    self.__register_otp()
                elif(task_val == '2'):
                    self.__validate_init()
                else:
                    print('잘못된 값을 입력하셨습니다.')
            except KeyboardInterrupt:
                exit(0)
            except Exception:
                exit(1)
        
    def __register_otp(self):
        
               
        user_name = input("사용자 이름을 입력하세요.(ex. User ID)::")
        
        
        key = pyotp.random_base32()
        print(f'key==>{key}')
        
        totp = pyotp.TOTP(key)
        
        qrvalue = totp.provisioning_uri(name=user_name, issuer_name='SampleOTP')
        
        # QR 코드 생성 호출
        self.__gen_qrcode(qrvalue)
        
        # Insert 사용자 데이터
        self.db.register_user(user_name=user_name, otp_key=key)     
        time.sleep(2)
        
        print('OTP 생성 완료')
        print('QR 코드는 output.html 파일을 확인하세요.')
        print(f'User Name:{user_name}')
        print(f'OTP Key:{key}')
        

      
        
    def __gen_qrcode(self, data):
        image = get_image(data)
        image.create_qr()
        
    def __validate_init(self):
        user_name = input("사용자 이름을 입력하세요.(ex. User ID)::")
        find_data = self.db.find_user(user_name=user_name)
        if(len(find_data) > 0 ):
            otp_key = find_data[0]['otp-key']
            self.__validate_otp(user_name=user_name,otp_key=otp_key)
        else:
            print('ID를 확인하세요.')
        
    def __validate_otp(self, user_name, otp_key):
        totp = pyotp.TOTP(otp_key)
        
        validate_key = input('생성된 OTP를 입력하세요==>')
        validate = totp.verify(validate_key)
        
        if(validate):
            print('유효한 OTP 입니다.')
        else:
            print('유효하지 않은 OTP 입니다.')
        
        
        
    # def validate_otp(self):
        
        
        
        
        
if __name__ == "__main__":
    print("OTP 연동 관리 Sample")
    print('종료는 Ctrl + C 누르세요.')
    m = main()
    m.task()
    
        