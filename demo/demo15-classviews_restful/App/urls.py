# urls.py  路由文件

from .exts import api
from .apis import *

# 路由
api.add_resource(HelloResouce, '/hello/')
api.add_resource(UserResource, '/user/', endpoint='id')
api.add_resource(User2Resource, '/user2/')
api.add_resource(User3Resource, '/user3/')
api.add_resource(User4Resource, '/user4/')


