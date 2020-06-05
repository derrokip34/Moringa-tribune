from django.test import TestCase
from .models import Editor,Article,tags
import datetime as dt

# Create your tests here.
class EditorTestClass(TestCase):

    #Setup Method
    def setUp(self):
        self.derrick = Editor(first_name = 'Derrick', last_name ='Kipruto', email ='derrickip34@gmail.com')

    #Test instance
    def test_instance(self):
        self.assertTrue(isinstance(self.derrick,Editor))

    #Testing save method
    def test_save_method(self):
        self.derrick.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors)>0)

class ArticleTestClass(TestCase):

    def setUp(self):
        #Creating a new editor
        self.derrick = Editor(first_name = 'Derrick', last_name ='Kipruto', email ='derrickip34@gmail.com')
        self.derrick.save_editor()

        #Create a new tag
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_article = Article(title = 'Test Article',post = 'This is a random test Post',editor = self.derrick)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()

    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news)>0)

    def test_get_news_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)