from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
# Create your models here.

class UserManager(models.Manager):
    
    def loginVal(self,postData):
        results = {'errors':[],'status': False, 'user': None}
        email_matches =self.filter(email=postData['email'])
        if len(email_matches)==0:
            results['errors'].append('Please check your email and try again!')
            results['status']=True
        else:
            results['user'] = email_matches[0]
            if not bcrypt.checkpw(postData['password'].encode(), results['user'].password.encode()):
                results['errors'].append('Please check your email and try it again!')
                results['status']=True
        return results
                
    
    def createUser (self,postData): #this function will be the function  to create a user
        password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
        print password
        self.create(name = postData['name'],email = postData['email'],password =password, birthday= postData['birthday'])

    def registerVal(self,postData):
        results = {'errors': [], 'status': False}

        if len(postData['name']) <2:
            results['status'] = True
            results['errors'].append(' Name is too short.')

        
        

        if not re.match(r"[^@]+@[^@]+\.[^@]+", postData['email']):
            results['status'] = True
            results['errors'].append('Email is not valid.')

        if len(postData['password']) <3:
            results['status'] = True
            results['errors'].append('Password is too short.')
        
        if postData['password'] != postData['c_password']:
            results['status'] = True
            results['errors'].append('Passwords do not match!')
        #check if email already exists
        user = self.filter(email= postData['email'])

        if len(user)>0:
            results['status'] = True
            results['errors'].append('This Email already exist in Database!')
            
        if len(postData['birthday'])<8:
            results['status'] = True
            results['errors'].append('Birthday not valid!')
        return results
            

       


class User(models.Model):
    name =models.CharField(max_length = 50)
    email =models.CharField(max_length = 50)
    password =models.CharField(max_length = 50)
    birthday= models.DateTimeField(null=True)
    objects = UserManager()