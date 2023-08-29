from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    @property
    def director_count(self):
        return self.director_set.count()


class Movie(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(max_length=300)
    duration = models.IntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE,
                                 null=True)

    def __str__(self):
        return self.title

    @property
    def rating(self):
        stars = [review.stars for review in self.reviews.all() if review.stars is not None]
        if not stars:
            return 0
        else:
            return round(sum(stars) / len(stars), 2)


STAR_CHOICES = (
    (1, '* '),
    (2, 2 * '* '),
    (3, 3 * '* '),
    (4, 4 * '* '),
    (5, 5 * '* ')
)


class Review(models.Model):
    text = models.TextField(max_length=310)
    product = models.ForeignKey(Movie, on_delete=models.CASCADE,
                                related_name='reviews')
    stars = models.IntegerField(default=0, choices=STAR_CHOICES)

    def __str__(self):
        return self.text
