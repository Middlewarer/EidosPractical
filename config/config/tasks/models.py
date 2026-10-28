from django.db import models

class Difficulties(models.IntegerChoices):
    HARD = 1, "Hard"
    MEDIUM = 2, "Medium"
    EASY = 3, "Easy"


class TaskStatuses(models.IntegerChoices):
    PUBLISHED = 1, "Published",
    DRAFT = 2, "Draft",
    ARCHIVED = 3, "Archived",

class Task(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    difficulty = models.IntegerField(choices=Difficulties.choices, default=Difficulties.EASY)
    status = models.IntegerField(choices=TaskStatuses.choices, default=TaskStatuses.DRAFT)
    academy_resourse = models.UUIDField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class AttemptStatuses(models.IntegerChoices):
    STARTED = 1, "Started"
    SUBMITTED = 2, "Submitted"
    PASSED = 3, "Passed"
    FAILED = 4, "Failed"

class Attempt(models.Model):
    user_id = models.UUIDField()
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    status = models.IntegerField(choices=AttemptStatuses.choices, default=AttemptStatuses.STARTED)
    started_at = models.DateTimeField(auto_now=True)
    submitted_at = models.DateTimeField()
    completed_at = models.DateTimeField()
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)


