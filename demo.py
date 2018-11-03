from core import Admin,Api,Auth,SPUser,Bucket

appid="hunks-blades-50d"
apikey="845c15d65938xxxxxxxxxxxx"
access_token = ""

# 第一次使用需要获取access_token
auth = Auth(appid, apikey)
access_token = auth.authorize('xxxxx@163.com', 'xxxxx')
print(access_token)

# admin 认证才具备修改删除权限
api = Admin(appid, access_token)

api.todo.new({'我的第一条消息':'测试UTF-8编码的中文支持程度', 'done': True})
api.todo.new({'second Message':'Thanks Simperium company', 'done': True})
t_list = api.todo.index()

print(t_list)
for txt in t_list['index']:
    # 查看所有信息
    text = api.todo.get(txt['id'])
    print(text)
    # print(api.todo.delete(txt['id']))

# user模式
user = SPUser(appid, access_token)
user.post({'age': 23})
user.post({'num': 24})
print(user.get())

# 显示全部信息
print(api.todo.all())
