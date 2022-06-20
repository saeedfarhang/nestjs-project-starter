import os
import settings

class ProjectStructure:
    def __init__(self, base_path,project_path):
        self.project_path = project_path
        self.base_path = base_path

    def basic_root_files_replace(self):
        document_title = input('document title: ')
        main_file_path = os.path.join(self.project_path, 'src/main.ts')
        self.manage_main_file(main_file_path,document_title)


    # this function handle main.ts file
    def manage_main_file(self, main_path,document_title):
        template_main_file= open(os.path.join(self.base_path, settings.basic_root_files_path, 'main.ts'))
        template_main_file_arr = template_main_file.readlines()
        template_main_file_arr[9] = template_main_file_arr[9].replace("{title}", document_title)    
        template_main_file_arr[10]=template_main_file_arr[10].replace("{title}", document_title)

        project_main_file = open(main_path, 'w')
        project_main_file.writelines(template_main_file_arr)

    def manage_configs(self):pass
        
        


        

