import filesrepo
import unittest

class FilesrepoTestCase(unittest.TestCase):

    def setUp(self):
        filesrepo.app.config['TESTING'] = True
        filesrepo.app.config['REPO_CONFIG'] = 'repos.yaml'
        self.app = filesrepo.app.test_client()

    # A repo that exists under REPO_DIR but not in repos.yaml should give
    # a 404 result
    def test_repo_not_in_config(self):
        rv = self.app.get('/java/')
        assert rv.status_code == 404

    # A repo that exists in repos.yaml but not under REPO_DIR should give 
    # a 404 result
    def test_repo_not_in_directory(self):
        rv = self.app.get('/bobbins/')
        assert rv.status_code == 404

    # A repo that exists in repos.yaml and in REPO_DIR should give 200
    def test_repo_in_config_and_directory(self):
        rv = self.app.get('/nexus/')
        assert rv.status_code == 200

    # A file that exists under repo should be returned
    # - if it has not changed upstream should be passed from filesystem
    # - if it has changed upstream should be redownloaded

    # A file that does not exist under repo but exists upstream should be 
    # returned



if __name__ == '__main__':
    unittest.main()
    
