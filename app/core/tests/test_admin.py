from django.test import TestCase, Client  # Client 用於在單元測試中，向應用程序發出測試請求
from django.contrib.auth import get_user_model
from django.urls import reverse  # 用於生成 Django 管理頁面的URL


class AdminSiteTests(TestCase):

    # 在執行每個測試前都需要完成的設置任務，可使用 setup 函數實現
    def setup(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@londonappdev.com',
            password='password123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@londonappdev.com',
            password='password123',
            name='Test user full name'
        )

    def test_users_listed(self):
        """Test that users are listed on the user page"""
        url = reverse('admin:core_user_changelist') # 建立 url，參數是想要的 url
        # core_user_changelist 是在 Django 管理文檔中定義的，此步驟將在資源中鏈接到該文檔
        # 使用 reverse 函數而不是手動輸入 URL 是因為如果將來想要更改 URL，
        # 就不必在測試中的任何地方進行更改，因為它應該自動更新基於 reverse。

        res = self.client.get(url) # 這將使用測試客戶端對這裡找到的 URL 執行 HTTP GET。

        # 檢查測試客戶端的名稱、信箱 HTTP 響應是 HTTP 200
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)