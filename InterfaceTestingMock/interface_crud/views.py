from django.shortcuts import render
from interface_crud.models import User, Article
from django.http import HttpRequest, JsonResponse
import json

# Create your views here.

# 新增文章
def add_article(request):
    if request.method == "POST":
        req = json.loads(request.body)
        print(req)

        key_flag = req.get('title') and req.get('content') and len(req) == 2
        # 判断请求体是否正确
        if key_flag:
            title = req['title']
            content = req['content']
            # title返回的是一个list
            title_exist = Article.objects.filter(title=title)
            # 判断是否存在同名的title
            if len(title_exist) != 0:
                return JsonResponse({"status": "BS.400", "msg": "title already exist, fail to publish."})
            """
            插入数据
            """
            add_art = Article(title=title, content=content, status='alive')
            add_art.save()
            return JsonResponse({"status": "BS.200", "msg": "publish article success."})
        else:
            return JsonResponse({"status": "BS.400", "message": "please check param."})

    # 查询文章

def modify_article():
    pass
