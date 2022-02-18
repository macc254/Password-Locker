class User:
    """
    A class that createsa an instance of users
    """
    user_list = [] #empty  user user_list
    
    def __init__(self,id,first_name,last_name)
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        
    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''
        
        User.user_list.append(self)
        
    @classmethod
    def delete_user(cls,number):
        '''
        delete_user method deletes user objects from user_list
        '''
        for user in cls.user_list:
            if user.id == number:
                return user.user_list.remove(number) 
            
               
    