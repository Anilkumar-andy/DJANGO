from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self,phone_number,password = None,**extra_fields):
        if not phone_number:
            raise ValueError("Phone Number is required")

        email = extra_fields.pop('email', None)  # Remove 'email' from extra_fields if present, or default to None
        if email:
            extra_fields['email'] = self.normalize_email(email)

        user=self.model(phone_number =phone_number,**extra_fields)
        user.set_password(password)
        user.save(using =self.db)
        return user
    
    def create_superuser(self,phone_number,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)            #setting some of the default fields as default while creating superuser so it can be created
        extra_fields.setdefault('is_superuser',True)        #setting some of the default fields as default while creating superuser so it can be created
        extra_fields.setdefault('is_active',True)           #setting some of the default fields as default while creating superuser so it can be created
        
        return self.create_user(phone_number,password,**extra_fields)       # calling create user function to set the rest of the values while keeping DRY concept of django