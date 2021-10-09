from django.db import models
import datetime

# class NFLPick(models.Model):
#     TEAMS_CHOICES = (
#         ("vikings", "Vikings"),
#         ("bears", "Bears"),
#     )
#     team = models.TextField(choices=TEAMS_CHOICES)


class DailyPicks(models.Model):
    pub_date = models.DateField("Date", default=datetime.date.today)

    # SPORTS_CHOICES = (
    #     ("nfl", NFLPick),
    #     ("mlb", "MLB"),
    #     ("other", "Other"), # This way, scores won't be rendered
    # )

    # league = models.TextField(choices=SPORTS_CHOICES)

    def __str__(self):
        return str(self.pub_date)

    class Meta:
        verbose_name = "Daily Pick"
        verbose_name_plural = "Daily Picks"

class ScottPick(models.Model):
    daily_picks = models.ForeignKey(DailyPicks, on_delete=models.CASCADE)
    pick_text = models.CharField(max_length=200)

    def __str__(self):
        return self.pick_text

    class Meta:
        verbose_name = "Scott's Pick"
        verbose_name_plural = "Scott's Picks"

class KanePick(models.Model):
    daily_picks = models.ForeignKey(DailyPicks, on_delete=models.CASCADE)
    pick_text = models.CharField(max_length=200)

    def __str__(self):
        return self.pick_text

    class Meta:
        verbose_name = "Kane's Pick"
        verbose_name_plural = "Kane's Picks"



# class TestChoice(models.Model):


#     class Meta:
#         verbose_name = "Test Choice"
#         verbose_name_plural = "Test Choices"