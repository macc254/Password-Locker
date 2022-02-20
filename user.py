class User:
    """
    A class that createsa an instance of users
    """
    user_list = [] #empty  user user_list
    
    def __init__(self,userId,first_name,last_name,username,password):
        self.userId = userId
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        
    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''
        User.user_list.append(self)
        
    def delete_user(self):
        '''
        delete_user method deletes user objects from user_list
        '''
        User.user_list.remove(self)
        
    @classmethod    
    def display_user(cls):
        '''
        display_user method displays users in the user_list
        '''
        return cls.user_list
               
    @classmethod
    def find_user_by_password(cls,number):
        '''
        find user by number will return the corresponding user of the number given
        '''
        for user in cls.user_list:
            if user.password == number:
                return user
    
    @classmethod
    def check_user_exists(cls,number):
        '''
        this method will use a number to check if the user exists
        '''
        for user in cls.user_list:
            if user.userId == number:
                    return True
        return False
        
        
    