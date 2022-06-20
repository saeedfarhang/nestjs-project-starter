import os
import settings


class SchemaManagement:
    def __init__(self, project_schema_file_path, base_path):
        self.project_schema_file_path = project_schema_file_path
        self.base_path = base_path

    def replace_schema_file(self):
        schema_content = open(os.path.join(self.base_path,settings.prisma_schema_path) )
        schema_content_arr = schema_content.readlines()

        schema_file = open(self.project_schema_file_path, 'w')
        schema_file.writelines(schema_content_arr)
 
    