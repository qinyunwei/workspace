import os
import pytest
if __name__ == '__main__':
    pytest.main()
    os.system('allure generate ./report/Allure_temp/ -o ./report/Allure_report/ --clean')

