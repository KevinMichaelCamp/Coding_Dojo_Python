from django.db import models
import bcrypt


class UserManager(models.Manager):
    def validate_register(self, postData):
        errors = {}

        if len(postData['name']) < 3:
            errors['name'] = "Name must be at least 3 characters"
        if len(postData['username']) < 3:
            errors['username'] = "Username must be at least 3 characters"
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters"
        if postData['password'] != postData['pw_confirm']:
            errors['pw_confirm'] = "Password must match confirmation"

        return errors

    def validate_login(self, postData):
        errors = {}

        if len(User.objects.filter(username=postData['username'])):
            user = User.objects.get(username=postData['username'])
            if bcrypt.checkpw(postData['password'].encode(), user.password):
                return errors
            else:
                errors['login'] = "Invalid username/password"
                return errors
        else:
            errors['login'] = "Invalid username/password"
            return errors


class ItemManager(models.Manager):
    def validate_item(self, postData):
        errors = {}

        if len(postData['name']) < 3:
            errors = "Item name must be at least 3 characters"

        return errors


class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.BinaryField(max_length=255)
    hire_date = models.DateField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "<User object: {} {} {}".format(self.name, self.username, self.hired_date)

    objects = UserManager()


class Item(models.Model):
    name = models.CharField(max_length=255)
    added_by = models.ForeignKey(User, related_name='added_by', on_delete=models.PROTECT)
    wished_by = models.ManyToManyField(User, related_name='wished_bys')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "<Item object: {} {}".format(self.name, self.added_by)

    objects = ItemManager()
