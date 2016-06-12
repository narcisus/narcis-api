import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

from narcis_api import models

class ModelsTestCase(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///models_test.db')
        models.Base.metadata.create_all(self.engine)
        self.DBSession = sessionmaker(bind=self.engine)
        self.session = self.DBSession()

        self.user = models.User(
            id=0,
            username='dan.stark',
            display_name='Dan Stark',
            first_name='Dan',
            last_name='Stark',
            email='dan.stark@email.net',
        )
        self.project = models.Project(
            id=1,
            name='Test Project',
            name_slug='test-project',
            private=True,
            url='http://test.domain.com/project/',
            user_id=0,
        )
        self.device = models.Device(
            id=2,
            name='Macbook Air',
            name_slug='macbook-air',
        )
        self.operating_system = models.OperatingSystem(
            id=3,
            name='OS X 10.9.5',
            name_slug='os-x-10-8-3',
        )
        self.browser = models.Browser(
            id=4,
            name='Chrome 43',
            name_slug='chrome-43',
        )
        self.platform = models.Platform(
            id=5,
            device_id=2,
            operating_system_id=3,
            browser_id=4,
            project_id=1,
        )
        self.page = models.Page(
            id=6,
            name='Test Page',
            name_slug='test-page',
            path='test/page/',
            project_id=1,
        )
        self.branch = models.Branch(
            id=7,
            name='master',
            name_slug='master',
            project_id=1,
        )
        self.build = models.Build(
            id=8,
            name='0000000',
            name_slug='0000000',
            branch_id=7,
        )
        self.screenshot = models.Screenshot(
            id=9,
            image='http://img.server.com/0000000',
            page_id=6,
            platform_id=5,
            build_id=8,
        )

    def tearDown(self):
        os.remove('models_test.db')

    def test_user_constructor(self):
        self.session.add(self.user)
        self.session.commit()
        assert(self.user.id == 0)
        assert(self.user.username == 'dan.stark')
        assert(self.user.display_name == 'Dan Stark')
        assert(self.user.first_name == 'Dan')
        assert(self.user.last_name == 'Stark')
        assert(self.user.email == 'dan.stark@email.net')

    def test_project_constructor(self):
        self.session.add(self.user)
        self.session.add(self.project)
        self.session.commit()
        assert(self.project.id == 1)
        assert(self.project.name == 'Test Project')
        assert(self.project.name_slug == 'test-project')
        assert(self.project.private == True)
        assert(self.project.url == 'http://test.domain.com/project/')
        assert(self.project.user_id == 0)
        assert(self.project.user == self.user)

    def test_device_constructor(self):
        self.session.add(self.device)
        self.session.commit()
        assert(self.device.id == 2)
        assert(self.device.name == 'Macbook Air')
        assert(self.device.name_slug == 'macbook-air')

    def test_operating_system_constructor(self):
        self.session.add(self.operating_system)
        self.session.commit()
        assert(self.operating_system.id == 3)
        assert(self.operating_system.name == 'OS X 10.9.5')
        assert(self.operating_system.name_slug == 'os-x-10-8-3')

    def test_browser_constructor(self):
        self.session.add(self.browser)
        self.session.commit()
        assert(self.browser.id == 4)
        assert(self.browser.name == 'Chrome 43')
        assert(self.browser.name_slug == 'chrome-43')

    def test_platform_constructor(self):
        self.session.add(self.device)
        self.session.add(self.operating_system)
        self.session.add(self.browser)
        self.session.add(self.user)
        self.session.add(self.project)
        self.session.add(self.platform)
        self.session.commit()
        assert(self.platform.id == 5)
        assert(self.platform.device_id == 2)
        assert(self.platform.operating_system_id == 3)
        assert(self.platform.browser_id == 4)
        assert(self.platform.project_id == 1)
        assert(self.platform.device == self.device)
        assert(self.platform.operating_system == self.operating_system)
        assert(self.platform.browser == self.browser)
        assert(self.platform.project == self.project)

    def test_page_constructor(self):
        self.session.add(self.user)
        self.session.add(self.project)
        self.session.add(self.page)
        self.session.commit()
        assert(self.page.id == 6)
        assert(self.page.name == 'Test Page')
        assert(self.page.name_slug == 'test-page')
        assert(self.page.path == 'test/page/')
        assert(self.page.project_id == 1)
        assert(self.page.project == self.project)

    def test_branch_constructor(self):
        self.session.add(self.user)
        self.session.add(self.project)
        self.session.add(self.branch)
        self.session.commit()
        assert(self.branch.id == 7)
        assert(self.branch.name == 'master')
        assert(self.branch.name_slug == 'master')
        assert(self.branch.project_id == 1)
        assert(self.branch.project == self.project)

    def test_build_constructor(self):
        self.session.add(self.branch)
        self.session.add(self.build)
        self.session.commit()
        assert(self.build.id == 8)
        assert(self.build.name == '0000000')
        assert(self.build.name_slug == '0000000')
        assert(self.build.branch_id == 7)
        assert(self.build.branch == self.branch)

    def test_screenshot_constructor(self):
        self.session.add(self.user)
        self.session.add(self.project)
        self.session.add(self.page)
        self.session.add(self.device)
        self.session.add(self.operating_system)
        self.session.add(self.browser)
        self.session.add(self.platform)
        self.session.add(self.build)
        self.session.add(self.screenshot)
        self.session.commit()
        assert(self.screenshot.id == 9)
        assert(self.screenshot.image == 'http://img.server.com/0000000')
        assert(self.screenshot.page_id == 6)
        assert(self.screenshot.platform_id == 5)
        assert(self.screenshot.build_id == 8)
        assert(self.screenshot.page == self.page)
        assert(self.screenshot.platform == self.platform)
        assert(self.screenshot.build == self.build)

if __name__ == '__main__':
    unittest.main()
