from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, mob_number, email, password, **extra_fields):
        """
        create and save  a User with the given email and password
        """
        if not email:
            raise ValueError(
                'The User must have an  email address')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            mob_number=mob_number,
            **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, mob_number, password, **extra_fields):
        """
        create and save a staff user with the given email and password
        """
        extra_fields.setdefault('is_superuser', False)
        user = self._create_user(
            email=email,
            mob_number=mob_number,
            password=password,

        )
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, mob_number, password, **extra_fields):
        """
        creates and saves a superuser with the given email and password
        """
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('SuperUser must have is_superuser =True')
        user = self._create_user(
            email=email,
            mob_number=mob_number,
            password=password,

        )
        user.is_staff = True
        user.admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user