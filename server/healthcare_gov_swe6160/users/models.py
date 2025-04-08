from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Default custom user model for Healthcare Gov SWE6160.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore[assignment]
    last_name = None  # type: ignore[assignment]

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
    

# class Doctor(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     specialization = models.CharField(max_length=255)
#     license_number = models.CharField(max_length=100, unique=True)
#     clinic_address = models.TextField()
#     is_available = models.BooleanField(default=True)

#     def __str__(self):
#         return f"Dr. {self.user.name} - {self.specialization}"
    
# class Appointment(models.Model):
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="appointments")
#     title = models.CharField(max_length=255)
#     description = models.TextField(blank=True)
#     appointment_date = models.DateTimeField()
#     duration_minutes = models.PositiveIntegerField(default=30)
#     is_booked = models.BooleanField(default=False)

#     def __str__(self):
#         return f"{self.title} with {self.doctor.user.name} on {self.appointment_date}"

# class Booking(models.Model):
#     patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="bookings")
#     appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
#     booked_at = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=50, choices=[
#         ("booked", "Booked"),
#         ("cancelled", "Cancelled"),
#         ("completed", "Completed"),
#     ], default="booked")

#     def __str__(self):
#         return f"Booking by {self.patient.name} for {self.appointment}"

# class Booking(models.Model):
#     patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="bookings")
#     appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
#     booked_at = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=50, choices=[
#         ("booked", "Booked"),
#         ("cancelled", "Cancelled"),
#         ("completed", "Completed"),
#     ], default="booked")

#     def __str__(self):
#         return f"Booking by {self.patient.name} for {self.appointment}"

