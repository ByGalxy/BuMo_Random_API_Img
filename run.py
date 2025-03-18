from flask import Flask, render_template
from routes.image_routes import image_bp  # 导入蓝图

app = Flask(__name__)

"""
创建时间： 2025.03.18
项目名称： 布莫随机API图/BuMo_Random_API_Img
作者名称： 布莫ByGalxy
"""

# 注册图片 API 蓝图
app.register_blueprint(image_bp)

# 主页路由
@app.route('/')
def index():
    return render_template('index.html')  # 渲染 index.html 页面

if __name__ == '__main__':
    app.run(debug=True)
