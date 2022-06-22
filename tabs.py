import pytest
import sys

@pytest.mark.usefixtures('driver')
class TestLink:
	def scroll_bottom():
		"""
		Create new tab, switch to it and switch back to old tab
		:return: None
		"""
		driver.get('https://www.lambdatest.com/')
		driver.maximize_window()
		driver.execute_script("window.open('about:blank','secondtab');")
		driver.switch_to.window("secondtab")
		driver.get('https://www.lambdatest.com/')
		driver.switch_to.window(1)
		assert True
	
