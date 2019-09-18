

import allure
class TestJen:
    @allure.step("模拟")
    def test_001(self):
        allure.attach("用户名","13344440000")
        assert True