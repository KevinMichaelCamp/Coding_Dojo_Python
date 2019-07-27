from django.db import models
import bcrypt


class UserManager(models.Manager):
    def validate_login(self, postData):
        errors = {}

        if len(User.objects.filter(username=postData['username'])):
            user = User.objects.get(username=postData['username'])
            if bcrypt.checkpw(postData['password'].encode(), user.password):
                return errors
            else:
                errors['password'] = "Password incorrect"
                return errors
        else:
            errors['username'] = "Username not found"
            return errors

    def validate_register(self, postData):
        errors = {}

        if len(postData['name']) < 3:
            errors['name'] = "Name must be at least 3 characters"
        if len(postData['username']) < 3:
            errors['username'] = "Username must be at least 3 characters"
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters"
        if postData['password'] != postData['pw_confirm']:
            errors['pw_confirm'] = "Password does not match confirmation"

        return errors


class ItemManager(models.Manager):
    def validate_item(self, postData):
        errors = {}

        if len(postData['item_name']) < 3:
            errors['item_name'] = "Item name must be at least 3 characters"

        return errors


class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.BinaryField(max_length=255)
    hire_date = models.DateField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "<User object: {} {} {}".format(self.name, self.username, self.hire_date)

    objects = UserManager()


class Item(models.Model):
    item_name = models.CharField(max_length=255)
    added_by = models.ForeignKey(User, related_name='items', on_delete=models.PROTECT)
    others = models.ManyToManyField(User, related_name='others_items', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "<Item object: {} {} {}".format(self.item_name, self.added_by, self.others)

    objects = ItemManager()
