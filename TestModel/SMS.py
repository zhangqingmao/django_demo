from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest

ACCESS_KEY_ID = ''  # 用户AccessKey  需要根据自己的账户修改
ACCESS_KEY_SECRET = ''  # Access Key Secret  需要根据自己的账户修改


class SMS:
    def __init__(self, signName, templateCode):
        self.signName = signName
        self.templateCode = templateCode  # 模板code
        self.client = client = AcsClient(ACCESS_KEY_ID, ACCESS_KEY_SECRET, 'cn-hangzhou')

    def send(self, phone_numbers, template_param):
        request = CommonRequest()
        request.set_accept_format('json')
        request.set_domain('dysmsapi.aliyuncs.com')
        request.set_method('POST')
        request.set_protocol_type('https')  # https | http
        request.set_version('2017-05-25')
        request.set_action_name('SendSms')

        request.add_query_param('RegionId', "cn-hangzhou")
        request.add_query_param('PhoneNumbers', phone_numbers)
        request.add_query_param('SignName', self.signName)
        request.add_query_param('TemplateCode', self.templateCode)
        request.add_query_param('TemplateParam', template_param)
        response = self.client.do_action_with_exception(request)
        return response

    def sendSms(phone,code):

        client = AcsClient('LTAIzBwTIyFYo6HQ', 'cbHknoQ6eSZopvvP7VjB0g5BRuKuFW', 'cn-hangzhou')
        request = CommonRequest()
        request.set_accept_format('json')
        request.set_domain('dysmsapi.aliyuncs.com')
        request.set_method('POST')
        request.set_protocol_type('https')
        request.set_version('2017-05-25')
        request.set_action_name('SendSms')
 
        request.add_query_param('RegionId', 'cn-hangzhou')
        request.add_query_param('PhoneNumbers', phone)
        request.add_query_param('SignName', '速运快递')
        request.add_query_param('TemplateCode', 'SMS_144456729')
        request.add_query_param('TemplateParam', '{"code":'+code+'}')
        response = client.do_action_with_exception(request)


# 短语发送对象
sms = SMS("速运快递", "SMS_144456729")
