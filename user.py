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
        
    
    