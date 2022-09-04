# @pytest.fixture(scope='function')
# def conncet_database():
#     print("连接数据库")
#     yield
#     print("断开数据库")
# 在每一个会话后清除已有的yaml数据
# @pytest.fixture(scope='session', autouse=True)
# def clear_yaml():
#     YamlUtil().clear_testcase_yaml('get_token.yml')