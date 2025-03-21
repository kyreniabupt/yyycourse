from selenium import webdriver
import selenium
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.brower = webdriver.Chrome()
    
    def tearDown(self):
        self.brower.quit()
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        # 张三听说有一个在线待办事项的应用
        # 他去看了这个应用的首页
        self.brower.get('http://localhost:8000')

        # 他注意到网页里包含'To-Do'这个词
        # assert 'To-Do' in brower.title
        self.assertIn('To-Do',self.brower.title) , "Browser title was " + self.brower.title
        self.fail('Finish the test!')
        
        # 应用有一个输入待办事项的文本输入框

        # 他在文本输入框中输入了“Buy flowers”

        # 他按了回车键后，页面更新了
        # 待办事项表格中显示了“1: Buy flowers”

        # 页面中又显示了一个文本输入框，可以输入其他待办事项
        # 他输入了“Send a gift to lisi”

        # 页面再次更新，他的清单中显示了这两个待办事项

        # 张三想知道这个网站是否会记住他的清单
        # 他看到网站为他生成了一个唯一的URL


        # 他访问这个URL，发现他的待办事项列表还在
        # 他满意的离开了

if __name__ == '__main__':
    unittest.main()
