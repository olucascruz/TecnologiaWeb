from django.db import models
from datetime import datetime

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    description = models.TextField(max_length=600)
    password = models.CharField(max_length=255)
    is_online = models.BooleanField()
    is_active = models.BooleanField()


class Candidate(User):
    profession = models.CharField(max_length=100)
    header = models.CharField(max_length=255)

class Recruiter(User):
    company = models.CharField(max_length=255)


class Resume(models.Model):
    candidate = models.OneToOneField(Candidate, on_delete=models.CASCADE, related_name="candidate")
    summary = models.TimeField(max_length=600)
    education = models.CharField(max_length=255)
    link_portfolio = models.CharField(max_length=255, null=True, blank=True, default= None)


class Language(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.CharField(max_length = 50)
    resume = models.ForeignKey(Resume, related_name = "languages", on_delete=models.CASCADE)


class WorkExpeience(models.Model):
    job_position = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    description_work = models.TextField(max_length=400, blank=True, null=True)
    resume = models.ForeignKey(Resume, related_name="work_experiences",on_delete=models.CASCADE)


class Certificate(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=600, null=True, blank=True)
    issued_by = models.CharField(max_length=200)
    issue_date = models.DateField()
    expiration_date = models.DateField(null=True, blank=True)
    favorite = models.BooleanField()
    resume = models.ForeignKey(Resume, related_name="certificates",on_delete=models.CASCADE)

class Skill(models.Model):
    title = models.CharField(max_length=255)
    favorite = models.BooleanField()
    resume = models.ForeignKey(Resume, related_name="skills", on_delete=models.CASCADE)

class JobVacancy(models.Model):
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    date_published = models.DateField(auto_now=True)
    description = models.TextField(max_length=600)
    views = models.PositiveBigIntegerField()
    candidate = models.ManyToManyField(Candidate, related_name="candidates")