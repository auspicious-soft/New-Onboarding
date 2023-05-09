from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        """
        Creates and saves a User with the given email,and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
    
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user
 
    def create_superuser(self, username, email, password=None):
       """
       Creates and saves a superuser with the given email, date of
       birth and password.
       """
       user = self.create_user(username, email, password=password)
       user.username = username
       user.role = 1
       user.is_superuser = True
       user.is_staff = True
       user.save()
       return user

