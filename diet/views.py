# coding: utf-8

from datetime import datetime, timedelta
from collections import Counter

from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.base import TemplateView
from django.conf import settings

from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException
from wechatpy.replies import TextReply
from wechatpy import parse_message, create_reply

from diet.models import Diet

MESSAGE_HELLO = u'''欢迎使用不挑食！
请直接回复您吃过的食物或者喝的饮料进行记录。
比如您刚刚喝了一瓶牛奶，就回复：牛奶。
请勿回复除食物或饮料以外的内容。'''
MESSAGE_WEEK_REPORT = u'您本周的饮食列表: \r\n'
MESSAGE_LINKS =u'''\r\n
<a href="{domain}{intro}">关于我们</a>'''

class DietManager(object):
    
    def get_links(self):
        return MESSAGE_LINKS.format(
            domain=settings.DOMAIN, 
            intro=reverse('intro'))

    def hello(self):
        return MESSAGE_HELLO

    def record_diet(self, content, openid):
        reply = self.analytic_diet(content, openid)
        if reply is not None:
            return reply
        foods = content.split()
        for i in foods:
            Diet(openid=openid, food=i).save()
        return self.analytic_diet('week', openid)

    def analytic_diet(self, content, openid):
        cmd = content.strip()
        if cmd == 'week':
            return self.week_report(openid) + self.get_links()

    def week_report(self, openid):
        now = datetime.now().date()
        start = now - timedelta(days=now.weekday())
        diets = Diet.objects.filter(openid=openid, created_at__gt=start)
        report = Counter([i.food for i in diets])
        return MESSAGE_WEEK_REPORT + u'\r\n'.join([u'{0}: {1}'.format(food, cnt) for food, cnt in report.iteritems()])

    def reply(self, msg):
        reply = TextReply(content=MESSAGE_HELLO, message=msg)
        if msg.type == 'event':
            reply = TextReply(content=self.hello(), message=msg)
        elif msg.type == 'text':
            content = self.record_diet(msg.content, msg.source)
            reply = TextReply(content=content, message=msg)
        return reply


class Wechat(View):

    def dispatch(self, *args, **kwargs):
        signature = self.request.GET.get('signature', '')
        timestamp = self.request.GET.get('timestamp', '')
        nonce = self.request.GET.get('nonce', '')

        try:
            check_signature(settings.TOKEN, signature, timestamp, nonce)
        except InvalidSignatureException:
            return HttpResponse(status=403)

        return super(Wechat, self).dispatch(*args, **kwargs)

    def get(self, request):
        echo_str = request.GET.get('echostr', '')
        return HttpResponse(echo_str)

    def post(self, request):
        msg = parse_message(request.body)
        dm = DietManager()
        return HttpResponse(dm.reply(msg).render())


class Intro(TemplateView):

    template_name = "diet/intro.html"
