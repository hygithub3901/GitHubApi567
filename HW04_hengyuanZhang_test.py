from HW04_hengyuanZhang import retrive_repo
from HW04_hengyuanZhang import retrive_commits
import unittest


class TestGitAPI(unittest.TestCase):
    def testRetrive_repo(self):
        self.assertEqual(retrive_repo('richkempinski')[0], 'csp')
        self.assertEqual(retrive_repo(''), None)

    def testRetrive_commits(self):
        self.assertEqual(retrive_commits('richkempinski', 'hellogitworld'), 30)
        self.assertEqual(retrive_commits('123', '456'), None)
        self.assertEqual(retrive_commits('richkempinski', '123'), 0)


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
