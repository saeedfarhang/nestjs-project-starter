from cmath import log
import os
from scripts.schema_manage import SchemaManagement
from scripts.structure import ProjectStructure
import settings
from scripts import copyenv

class NestCommands:
    def __init__(self) -> int:
        self.project_name = settings.project_name
        self.base_projects_path = settings.base_projects_path
        self.project_path = os.path.join(settings.base_projects_path, settings.project_name)
        self.base_path = os.getcwd()

    def createProject(self,):
        print(f"create new project with name of {self.project_name}")
        try:
            os.makedirs(self.base_projects_path)
        except OSError as error: 
            print(f"warining: error in creating project dir. it probebly because dir name is existing in {self.project_path}")
        finally:
            os.chdir(self.base_projects_path)
        os.system(f"nest new {self.project_name}")
        
        os.chdir(self.project_name)
        os.system('yarn add prisma')
        os.system('yarn prisma init')

    def replaceEnv(self):
        env_content = copyenv.create_env(self.base_path)
        copyenv.replace_env(self.project_path, env_content)
    
    def editPrismaSchema(self, ):
        project_prisma_schema = os.path.join(self.project_path, "prisma/schema.prisma")
        schemaManagement = SchemaManagement(project_prisma_schema, self.base_path)
        schemaManagement.replace_schema_file()

    def editBaseFiles(self,):
        structure = ProjectStructure(self.base_path, self.project_path)
        structure.basic_root_files_replace()
        

if __name__ == '__main__':
    nest = NestCommands()
    nest.createProject()
    nest.replaceEnv()
    nest.editPrismaSchema()
    nest.editBaseFiles()