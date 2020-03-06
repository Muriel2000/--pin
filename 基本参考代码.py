from flask import Flask, request, make_response          # 引用各个模块
from httpapi.HTTPSDK import *	#两个必要的包

class sys_state():                       # 定义系统状态这一类
    def __init__(                        # 定义类的属性
            self,                   # 它的属性有：
            start_time_in=0,                  # 开始时间
            saving=0,                         # 当用户输入save，自动保存当前所有数据
            system_state=0,                   # 系统状态
            print_number=0,                   # 打印编号
            user_number=0,                    # 用户编号
            file_number=0,                    # 文件个数
            recharge_number=0                 # 充值次数
    ):
        self.saving = saving
        self.system_state = system_state
        self.print_number = print_number
        self.user_number = user_number
        self.start_time = start_time_in
        self.file_number = file_number
        self.recharge_number = recharge_number

    def read(dic):                       # 定义类的方法（函数）————从dic（字典数据结构）读取信息（定义类的属性）并返回这些信息
        return sys_state(start_time_in=dic['start_time'], saving=dic['saving'], system_state=dic['system_state'],
                         print_number=dic['print_number'], user_number=dic['user_number'],
                         file_number=dic['file_number'], recharge_number=dic['recharge_number'])
class user_infomation():                 # 定义用户信息这一类
    def __init__(                        # 定义类的属性
            self,                     # 它的属性有：
            user_id=None,                        # 用户ID（QQ号）
            Numtime=0,                           # 当前时间--从1970年一月一日到现在的秒数
            user_state=0,                        # 用户状态
            file_size=0,                         # 文件大小
            money=0,                             # 消费金额
            user_level=0                         # 用户等级

    ):
        self.user_state = user_state
        self.user_level = user_level
        self.user_id = user_id
        self.money = money
        self.Numtime = Numtime
        self.file_size = file_size
        self.print_record_list = {}
        self.recharge_list = {}
        self.file_list = {}
        return

    def read(dic):                      # 定义类的方法（函数）————从dic（字典数据结构）读取信息（定义类的属性）并返回这些信息
        return user_infomation(user_state=dic['user_state'], user_level=dic['user_level'], user_id=dic['user_id'],
                         money=float(dic['money']), Numtime=float(dic['Numtime']), file_size=dic['file_size'])
# 配置路由，在插件提交返回中配置地址（如本例 http://127.0.0.1:5000）
# ----------------------------------------------保存单个用户函数------------------------------------------------
def Save_User_date_one_first(user_id):                                        # 保存一个用户
    if os.path.exists('date\\User_infomation\\' + str(user_id)) == False:     # 判断这个用户数据是否存在或一致
        os.mkdir('date\\User_infomation\\' + str(user_id))                    # 修改用户数据
    dic_temp = {}                                                             # 创建一个新的空的字典数据结构
    dic_temp['user_id'] = dic_user_infomation[str(user_id)].user_id           # 加入user_id信息
    dic_temp['user_state'] = dic_user_infomation[str(user_id)].user_state     # 加入user_state信息
    dic_temp['user_level'] = dic_user_infomation[str(user_id)].user_level     # 加入user_level信息
    dic_temp['money'] = dic_user_infomation[str(user_id)].money               # 加入money信息
    dic_temp['Numtime'] = dic_user_infomation[str(user_id)].Numtime           # 加入Numtime信息
    dic_temp['file_size'] = dic_user_infomation[str(user_id)].file_size       # 加入file_size信息
    file = open('date\\User_infomation\\' + str(user_id) + '\\User_infomation.txt', 'w')  # 打开对应user_id的date\\User_infomation\\和\\User_infomation.txt文件（以只写的方式）
    file.write(json.dumps(dic_temp))                                          # 向文件中写入字典数据结构
    file.close()                                                              # 关闭文件
    Save_User_Print_record(user_id)                                           # 调用函数保护充值列表
    Save_User_recharge_list(user_id)                                          # 调用函数保护文件列表
    Save_User_file_list(user_id)                                              # 调用函数保护用户列表
    return
# --------------------------------------------用户数据更新函数------------------------------------------------
def Save_User_date():                                                         # 按照现在使用过的用户进行更新
    for user_id in user_list:                                                 # 进入循环（一个一个用户数据按编号更新）
        if os.path.exists('date\\User_infomation\\' + str(user_id)) == False: # 判断这个用户数据是否存在或一致
            os.mkdir('date\\User_infomation\\' + str(user_id))                # 修改用户数据
        dic_temp = {}                                                         # 创建一个新的空的字典数据结构
        dic_temp['user_id'] = dic_user_infomation[str(user_id)].user_id       # 加入user_id信息
        dic_temp['user_state'] = dic_user_infomation[str(user_id)].user_state  # 加入user_state信息
        dic_temp['user_level'] = dic_user_infomation[str(user_id)].user_level  # 加入user_level信息
        dic_temp['money'] = dic_user_infomation[str(user_id)].money           # 加入money信息
        dic_temp['Numtime'] = dic_user_infomation[str(user_id)].Numtime       # 加入Numtime信息
        dic_temp['file_size'] = dic_user_infomation[str(user_id)].file_size   # 加入file_size信息
        file = open('date\\User_infomation\\' + str(user_id) + '\\User_infomation.txt', 'w')  # 打开对应user_id的date\\User_infomation\\和\\User_infomation.txt文件（以只写的方式）
        file.write(json.dumps(dic_temp))                                      # 向文件中写入字典数据结构
        file.close()                                                          # 关闭文件
        Save_User_Print_record(user_id)                                       # 调用函数保护充值列表
        Save_User_recharge_list(user_id)                                      # 调用函数保护文件列表
        Save_User_file_list(user_id)                                          # 调用函数保护用户列表
    return
#--------------------------------------加载用户------------------------------------------------------------
def load_User_date_Success(sdk):
    if sdk != 1:                                    # 显示以下内容
        massage='感谢您进入内测，我们给您的账户添加了10元，仅在内测阶段使用\n\n内测阶段打印机可能出现各种故障，我们不建议您现在将他当作正式的服务使用。\n\n您发送的一切消息都会被记录下来作为参考使用。\n\n欢迎您提出各种建议\n\n您可以发送\n建议 （您的建议内容）\n给机器人\n或者联系qq：794358907\ntel：15767788124\n\n注：(打印机失去连接和充值不到位暂时属于正常现象)\n\n再次感谢您参与我们的测试。\n\n'
        recharge_money(sdk.getMsg().QQ,10,sdk.getMsg().QQ,time.time())
        sdk.sendPrivdteMsg(sdk.getMsg().QQ, massage)
        sdk.sendPrivdteMsg(sdk.getMsg().QQ, '欢迎您第一次使用油印智能打印系统 输入 帮助 获得详细帮助')
        sdk.sendPrivdteMsg(sdk.getMsg().QQ, '您的身份档案已建立\n用户创建时间' + str(dic_user_infomation[str(sdk.getMsg().QQ)].Numtime))
    return
# --------------------------------------------用户数据更新函数------------------------------------------------
def Save_User_date():                                                         # 按照现在使用过的用户进行更新
    for user_id in user_list:                                                 # 进入循环（一个一个用户数据按编号更新）
        if os.path.exists('date\\User_infomation\\' + str(user_id)) == False: # 判断这个用户数据是否存在或一致
            os.mkdir('date\\User_infomation\\' + str(user_id))                # 修改用户数据
        dic_temp = {}                                                         # 创建一个新的空的字典数据结构
        dic_temp['user_id'] = dic_user_infomation[str(user_id)].user_id       # 加入user_id信息
        dic_temp['user_state'] = dic_user_infomation[str(user_id)].user_state  # 加入user_state信息
        dic_temp['user_level'] = dic_user_infomation[str(user_id)].user_level  # 加入user_level信息
        dic_temp['money'] = dic_user_infomation[str(user_id)].money           # 加入money信息
        dic_temp['Numtime'] = dic_user_infomation[str(user_id)].Numtime       # 加入Numtime信息
        dic_temp['file_size'] = dic_user_infomation[str(user_id)].file_size   # 加入file_size信息
        file = open('date\\User_infomation\\' + str(user_id) + '\\User_infomation.txt', 'w')  # 打开对应user_id的date\\User_infomation\\和\\User_infomation.txt文件（以只写的方式）
        file.write(json.dumps(dic_temp))                                      # 向文件中写入字典数据结构
        file.close()                                                          # 关闭文件
        Save_User_Print_record(user_id)                                       # 调用函数保护充值列表
        Save_User_recharge_list(user_id)                                      # 调用函数保护文件列表
        Save_User_file_list(user_id)                                          # 调用函数保护用户列表
    return
def Get_massage(sdk):
    # logging.info('收到消息 ' +sdk.getMsg().Msg+ ' Form ' + str(sdk.getMsg().QQ))
    print(sdk.getMsg().Msg)                                         # 打印信息
    sdk.sendPrivdteMsg(sdk.getMsg().QQ, sdk.getMsg(),Msg)           # 显示信息
    print(sdk.getMsg().Msg)                                         # 打印信息
    return
    logging.exception("收到消息 " + sdk.getMsg().QQ + '   的   '+ sdk.getMsg().Msg)  # 显示信息
    if state.system_state == 3:                                     # 若系统状态异常
        sdk.sendPrivdteMsg(sdk.getMsg().QQ, '系统维护中。。。请稍后再试。。。')  # 显示信息
        return
    if sdk.getMsg().QQ not in last_user_massage:   # last_user_massage为字典数据结构，查找该数据结构中是否有sdk.getMsg().QQ这个键
        last_user_massage[sdk.getMsg().QQ]=time.time()  # 创建并更新用户发送最后一条消息的时间戳
    else:
        if time.time() - last_user_massage[sdk.getMsg().QQ] >300:  # 用当前时间戳减去用户最后一条消息的时间戳，看是否超过5分钟
            if sdk.getMsg().QQ in dic_user_infomation:    # 若超过5分钟，就删除储存用户信息的几个临时数据结构
                del dic_user_infomation[sdk.getMsg().QQ]   # 对应的用户信息
            if sdk.getMsg().QQ in tem_print_list:          # 打印列表
                del tem_print_list[sdk.getMsg().QQ]
            if sdk.getMsg().QQ in user_state:              # 用户状态
                del user_state[sdk.getMsg().QQ]
            last_user_massage[sdk.getMsg().QQ] = time.time()         # 更新用户最后一条消息的时间戳
    if str(sdk.getMsg().QQ) not in dic_user_infomation:              # 若不存在则创建并且更新
        load_User_date(sdk.getMsg().QQ,sdk)                          # 载入用户
    if sdk.getMsg().QQ not in user_state:                            # 若不存在则先将用户状态变为正常状态
        user_state[sdk.getMsg().QQ] = 0
    if sdk.getMsg().Type == 1:                                       # 若用户发送的是普通消息
        if sdk.getMsg().Msg == '重启':                                # 若发送信息是重启
            if sdk.getMsg().QQ in dic_user_infomation:               # 就删除储存用户信息的几个临时数据结构
                del dic_user_infomation[sdk.getMsg().QQ]
            if sdk.getMsg().QQ in tem_print_list:
                del tem_print_list[sdk.getMsg().QQ]
            if sdk.getMsg().QQ in user_state:
                del user_state[sdk.getMsg().QQ]
            last_user_massage[sdk.getMsg().QQ] = time.time()          # 更新用户最后一条消息的时间戳
            sdk.sendPrivdteMsg(sdk.getMsg().QQ, '重启成功！')          # 显示信息
            return

        if user_state[sdk.getMsg().QQ] == 1:                          # 若用户状态为1
            receive_add_tem_print(sdk)                                # 调用添加临时打印列表函数
            return
        if user_state[sdk.getMsg().QQ] == 2:                          # 若用户状态为2
            receive_del_tem_print(sdk)                                # 调用删除临时打印列表函数
            return
        if user_state[sdk.getMsg().QQ] == 3:                          # 若用户状态为3
            receive_del_file(sdk)                                     # 调用删除文件表函数
            return
        if sdk.getMsg().Msg.find('帮助') != -1:                       # 判断用户发送消息中有无‘帮助’
            Help(sdk)                                                 # 调用帮助界面函数
            return
        if sdk.getMsg().Msg.find('save') != -1:                       # 判断用户发送消息中有无‘save’
            sdk.sendPrivdteMsg(sdk.getMsg().QQ, '保存中。。。')
            Save_date()                                               # 调用保存文件总函数
            sdk.sendPrivdteMsg(sdk.getMsg().QQ, '保存完成！')
            return
        if sdk.getMsg().Msg.find('上传文件') != -1:                    # 判断用户发送消息中有无‘上传文件’
            sdk.sendPrivdteMsg(sdk.getMsg().QQ, '请直接发文件给我！')
        if sdk.getMsg().Msg.find('关于') != -1:                        # 判断用户发送消息中有无‘关于’
            sdk.sendPrivdteMsg(sdk.getMsg().QQ, '作者葡调皮~，欢迎与我联系哦！ QQ:794358907')
            return
        if sdk.getMsg().Msg.find('建议') != -1:                        # 判断用户发送消息中有无‘建议’
            sdk.sendPrivdteMsg(sdk.getMsg().QQ, '感谢您的建议！十分感谢！！')
            logging.exception(sdk.getMsg().Msg)
            return


        if sdk.getMsg().Msg.find('打印列表') != -1:                     # 判断用户发送消息中有无‘打印列表’
            if sdk.getMsg().Msg.find('添加') != -1:                     # 判断用户发送消息中有无‘添加’
                add_tem_print(sdk)                                      # 调用添加临时打印列表函数
                return
            if sdk.getMsg().Msg.find('删除') != -1:                     # 判断用户发送消息中有无‘删除’
                del_tem_print(sdk)                                      # 调用删除临时打印列表函数
                return
            if sdk.getMsg().Msg.find('查询') != -1:                     # 判断用户发送消息中有无‘查询’
                tem_print(sdk)                                          # 调用打印列表文件函数
                return
        if sdk.getMsg().Msg.find('打印文件') != -1:
            if sdk.getMsg().Msg.find('添加') != -1:                      # 打印列表添加
                add_tem_print(sdk)
                return
            if sdk.getMsg().Msg.find('删除') != -1:
                del_tem_print(sdk)
                return
            if sdk.getMsg().Msg.find('查询') != -1:
                tem_print(sdk)
                return
            print_page(sdk,sdk.getMsg().QQ)
            return
        if sdk.getMsg().Msg.find('文件') != -1:                          # 判断用户发送消息中有无‘文件’
            if sdk.getMsg().Msg.find('添加') != -1:
                add_tem_print(sdk)                                       # 调用添加临时打印列表 函数
                return
            if sdk.getMsg().Msg.find('删除') != -1:
                del_file(sdk)                                            # 调用删除文件表函数
                return
            if sdk.getMsg().Msg.find('查询') != -1:
                User_file_list(sdk)                                      # 显示储存文件信息
                return
        if sdk.getMsg().Msg.find('充值') != -1:                          # 判断用户发送消息中有无‘充值’
            way2recharge(sdk)                                            # 调用充值方法函数
            return
        if sdk.getMsg().Msg.find('打印') != -1:                          # 判断用户发送消息中有无‘打印’
            print_page(sdk,sdk.getMsg().QQ)                              # 调用打印文件总函数
            return
        if sdk.getMsg().Msg.find('个人信息') != -1:                       # 判断用户发送消息中有无‘个人信息’
            tem='用户信息：'                                              # 传递个人信息
            tem+='\n用户建立时间：'+str(dic_user_infomation[sdk.getMsg().QQ].Numtime)
            tem+='\n余额：'+str(dic_user_infomation[sdk.getMsg().QQ].money)
            try:
                if len(dic_user_infomation[sdk.getMsg().QQ].file.size) !=0:
                    tem += '\n用户文件数：' + str(len(dic_user_infomation[sdk.getMsg().QQ].file.size))
                else:
                    tem += '\n用户文件数：0'
            except:
                tem +='\n用户文件数：0'
            sdk.sendPrivdteMsg(sdk.getMsg().QQ, tem)                       # 显示个人信息

        if sdk.getMsg().Msg.find('system') != -1:                          # 判断用户发送消息中有无‘system’
            sdk.sendPrivdteMsg(sdk.getMsg().QQ, 'file_number'+ str(state.file_number)+'\n')  # 显示信息
            sdk.sendPrivdteMsg(sdk.getMsg().QQ, 'print_number' + str(state.print_number) + '\n')  # 显示信息
            sdk.sendPrivdteMsg(sdk.getMsg().QQ, 'user_number' + str(state.user_number) + '\n')  # 显示信息
        sdk.sendPrivdteMsg(sdk.getMsg().QQ, '您发送的消息为' + sdk.getMsg().Msg+'\n输入 \'帮助\' 获得帮助')  # 显示信息
        print(sdk.getMsg().Msg)
    if sdk.getMsg().Type == 105:                                            # 判断发送消息是否为文件消息
        file_get(sdk)                                                       # 调用文件判断函数
        return

# --------------------------------------------------正式运行--------------------------------------------------------
# logging.info('正式运行')
#load_System_state()
app = Flask(__name__)
#logging.basicConfig(filename="test.log", filemode="a", format="%(asctime)s %(name)s:%(levelname)s:%(message)s", datefmt="%d-%M-%Y %H:%M:%S", level=logging.DEBUG)
# address=0
#logging.exception("开始")
# sending_list=[]

@app.route('/', methods=['GET', 'POST'])
def index():
#    logging.exception("收到请求 " )
    req = request.get_data()
    print(req)

    sdk = HTTPSDK.httpGet(req)
    Get_massage(sdk)

    return make_response(sdk.toJsonString())
# @app.route('/hello', methods=['GET', 'POST'])
# def hello():
#
#     tradeNo=request.form.get('tradeNo')
#     Money = request.form.get('Money')
#     title = request.form.get('title')
#     logging.exception("充值记录    "+str(title) + '    '+str(Money)+'    '+str(tradeNo))
#     print(title)
#     print(Money)
#     print(tradeNo)
#     if os.path.exists('date\\User_infomation\\' + str(title)) == False:
#         recharge_money(user_id=794358907,Numtime=time.time(),money=Money,number=tradeNo)
#         return 'Fail'
#     if title not in dic_user_infomation:
#         load_User_date_no_answer(title)
#     if str(tradeNo) in dic_user_infomation[str(title)].recharge_list:
#         return 'Fail'
#     recharge_money(user_id=title,Numtime=time.time(),money=Money,number=tradeNo)
#     push = HTTPSDK.httpPush("http://127.0.0.1:5001")
#     push.sendPrivdteMsg(title, '您充值的'+str(Money)+'元已到账！')
#     push.sendPrivdteMsg(title, '现在余额为' + str(dic_user_infomation[title].money) + '元！')
#     # if title in dic_user_infomation:
#     #     del dic_user_infomation[title]
#     # if title in tem_print_list:
#     #     del tem_print_list[title]
#     # if title in user_state:
#     #     del user_state[title]#暂时还没搞明白为什么充值后会炸
#     return 'Success'

#
#
# thread1 = threading.Thread(target=get_connect)
#
# # 开启新线程
# logging.exception("监听")
# # thread2 = threading.Thread(target=app.run(),args=())
# thread1.start()
app.run(host='0.0.0.0',port=8010)