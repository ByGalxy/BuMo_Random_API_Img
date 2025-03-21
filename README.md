以下内容使用AI翻译

简体中文 | [English](README_en.md) 

## 使用教程

需要下载python，然后下载flask库

```
pip install flask
```

下载源码后

### 添加图片

图片我就不提供了，然后图片要添加到static/images/Honkai_Star_Rail

例如：
 - 横屏图片添加到h
 - 竖屏图片添加到s

## 预览运行效果

我正常运行后是这样的

```
PS D:\xianmu\1> python run.py
 * Serving Flask app 'run'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 104-608-534
```

浏览器访问http://127.0.0.1:5000，可以看到能访问到templates/index.html

如果访问我们刚刚添加到的图片，比如：

`http://127.0.0.1:5000/random_image/` + <名字>

`http://127.0.0.1:5000/random_image/崩坏星穹铁道`

如果直接访问`http://127.0.0.1:5000/random_image/崩坏星穹铁道`会随机访问目录下的`h`和`s`目录

如果要直接访问`h`或者`s`目录，比如：

`h`目录：`http://127.0.0.1:5000/random_image/崩坏星穹铁道?hsp=h`

或者

`s`目录：`http://127.0.0.1:5000/random_image/崩坏星穹铁道?hsp=s`

## 添加更多分类

这个模板代码可以添加更多分类目录

可以查看routes/image_routes.py的代码，然后找到：
```python
# 预设类别
CATEGORIES = {
    "崩坏星穹铁道": os.path.join(IMAGE_DIR, "Honkai_Star_Rail")
}
```

可以参考`"崩坏星穹铁道": os.path.join(IMAGE_DIR, "Honkai_Star_Rail")`添加更多的分类，例如：

```python
CATEGORIES = {
    "崩坏星穹铁道": os.path.join(IMAGE_DIR, "Honkai_Star_Rail"),
    "崩坏3": os.path.join(IMAGE_DIR, "Honkai3"),
    ...
}
```

然后在目录添加刚刚新增的分类，比如我要创建`Honkai3`，可以参考`Honkai_Star_Rail`目录的创建方式
