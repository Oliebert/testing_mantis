from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_project_page(self):
        wd = self.app.wd
        #if not (wd.current_url.endswith("/manage_proj_page.php")):
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_xpath("//div/div[4]/div[1]/ul/li[2]/a").click()

    def create_project(self, project):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_css_selector("input.button-small").click()
        self.fill_project_form(project)
        wd.find_element_by_xpath("//span[@class='submit-button']/input").click()
        #self.project_cache = None

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_project_form(self, project):
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.description)

   # project_cache = None

    def get_projects_list(self):
        #if self.project_cache is None:
        wd = self.app.wd
        project_list = []
        self.open_project_page()

        rows = wd.find_elements_by_xpath("//div/div[4]/div[2]/table/tbody/tr")
        for row in rows:
            cells = row.find_elements_by_tag_name("td")
            name = cells[0].text
            description = cells[4].text
            project_list.append(Project(name=name, description=description))

        return list(project_list)

    def select_project_by_name(self, name):
        wd = self.app.wd
        wd.find_element_by_link_text("%s" % name).click()

    def delete_project(self, project):
        wd = self.app.wd
        self.open_project_page()
        self.select_project_by_name(project)
        wd.find_element_by_xpath("//form[@id='project-delete-form']/fieldset/input[3]").click()
        wd.find_element_by_xpath("//div[@id='content']/div/form/input[4]").click()











