from django.db import models
from django.contrib.auth.models import User


class Set(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    term_language = models.CharField(
        max_length=100, null=True, blank=True, default='English')
    definition_language = models.CharField(
        max_length=100, null=True, blank=True, default='English')
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        User, related_name='sets', on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.name)

    @property
    def total_cards(self):
        cards = self.card_set.all()
        total = len(cards)
        return total


NUM_BOXES = 5
BOXES = range(1, NUM_BOXES+1)


class Card(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    card_set = models.ForeignKey(Set, on_delete=models.CASCADE, null=True)
    box = models.IntegerField(
        choices=zip(BOXES, BOXES),
        default=BOXES[0]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        User, related_name='cards', on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.question)

    def move(self, solved):
        new_box = self.box + 1 if solved else BOXES[0]

        if new_box in BOXES:
            self.box = new_box
            self.save()

        return self


"""
    The zip() function returns a zip object, which is an iterator of tuples where the first 
    item in each passed iterator is paired together, and then the second item in each passed 
    iterator are paired together etc.
"""
