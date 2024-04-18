import json,time


class db_handler:
    """
    JSON Data Handler

    ...

    Info.
    -----
    Date: 20240418
    
    by. MBHAN    
    
    Methods
    -------
    register_user(user_name, otp_key)
        사용자 등록 처리
        
    find_user(user_name)
        단일 사용자 정보 조회
    """
    
    __file_name = 'user_list.json'
    __init_data = {
                    "list": [] 
                    }
                
    data = None
    def __init__(self):
        
        try:            
            self.__readfile()
            
        except json.decoder.JSONDecodeError:
            pass
        except FileNotFoundError:
            with open(self.__file_name, 'w') as file:
                json.dump(self.__init_data, file)
                print('==>Init Data Completed')
                self.data = self.__init_data
                
    def __readfile(self):
        with open(self.__file_name,'r') as file:
                self.data = json.load(file)
                print('==>Read User List')
                
    def __savefile(self):
         with open(self.__file_name, 'w') as file:
                json.dump(self.data, file)
                print('==>Data Update Completed')
                
    def register_user(self, user_name, otp_key):
        self.data['list'].append({'username':user_name, 'otp-key':otp_key})
        self.__savefile()
    
    def find_user(self, user_name):
        
        return list(filter(lambda x:x["username"]==user_name,self.data["list"]))
        
        
 