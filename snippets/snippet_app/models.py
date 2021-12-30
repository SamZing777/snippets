from django.db import models
from django.contrib.auth import get_user_model
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

User = get_user_model()

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=100, blank=True)
	code = models.TextField()
	linenos = models.BooleanField(default=False)
	language = models.CharField(choices=LANGUAGE_CHOICES, default='python',
								max_length=100)
	style = models.CharField(choices=STYLE_CHOICES, default='friendly',
								max_length=100)
	highlighted = models.TextField(default="Highlighted text fields here..")
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['created']

	def save(self, *args, **kwargs):

	# Use pygments lib to create a highlighted HTML representation of the code snippet
	
		lexer = get_lexer_by_name(self.language)
		linenos = 'table' if self.linenos else False
		options = {'title': self.title} if self.title else {}
		formatter = HtmlFormatter(style=self.style, linenos=linenos,
									full=True, **options)
		self.highlighted = highlight(self.code, lexer, formatter)
		super().save(*args, **kwargs)

	def __str__(self):
		return self.title
