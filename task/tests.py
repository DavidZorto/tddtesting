from django.test import TestCase
from .models import Task
# Create your tests here.

class TaskModelTest(TestCase):
    def test_task_model_exists(self):
        task = Task.objects.count()
        self.assertEqual(task, 0)
    def test_model_has_string_represenation(self):
        task= Task.objects.create(title="First Task")
        self.assertEqual(str(task), task.title)


class IndexPageTest(TestCase):
    def test_index_page_returns_correct_response(self):
        response= self.client.get('/')

        self.assertTemplateUsed(response, 'task/index.html')
        self.assertEqual(response.status_code, 200)
    
    def test_index_page_returns_tasks(self):
        tasks= Task.objects.create(title="First Task")
        response= self.client.get('/')
        self.assertContains(response, tasks.title)

class DetailPage(TestCase):
    def setUp(self):
        self.task = Task.objects.create(title='First Task', description='The Description')

    def test_detail_page_returns_correct_response(self):
        response= self.client.get(f'/{self.task.id}/')

        self.assertTemplateUsed(response, 'task/detail.html')
        self.assertEqual(response.status_code, 200) 
   
    def test_page_has_correct_content(self):
        response= self.client.get(f'/{self.task.id}/')
        self.assertContains(response, self.task.title)
        self.assertContains(response, self.task.description)

