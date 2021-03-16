from unittest import mock
import HW04_hengyuanZhang


@mock.patch('HW04_hengyuanZhang.retrive_repo')
def mock_retrive_repo_function(mock_retrive_repo_func):
    print(mock_retrive_repo_func)

mock_retrive_repo_function()