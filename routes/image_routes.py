import os
import random
from flask import Blueprint, send_file, jsonify, request, render_template

image_bp = Blueprint('image', __name__)  # 创建蓝图

# 定义图片存放目录
IMAGE_DIR = "static/images"

# 预设类别
CATEGORIES = {
    "崩坏星穹铁道": os.path.join(IMAGE_DIR, "Honkai_Star_Rail")
}

# 自定义 404 页面
@image_bp.app_errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@image_bp.route('/random_image/<category>')
def random_image(category):
    # 检查类别是否有效
    if category not in CATEGORIES:
        return jsonify({"error": "Invalid category"}), 400

    base_path = CATEGORIES[category]

    # 解析 hsp 参数（可能的值："h"（横屏）、"s"（竖屏））
    hsp = request.args.get("hsp")

    if hsp not in ["h", "s", None]:  # 如果 hsp 不是 h、s 或 None，返回错误
        return jsonify({"error": "Invalid hsp parameter"}), 400

    # 如果 hsp 为空，则随机选择 h 或 s
    search_order = [hsp] if hsp else random.sample(["h", "s"], 2)  # 随机排列 h、s

    for folder in search_order:
        category_path = os.path.join(base_path, folder)

        # 检查目录是否存在
        if not os.path.exists(category_path):
            continue  # 如果该目录不存在，尝试下一个

        # 获取该类别的所有图片文件
        images = [f for f in os.listdir(category_path) if f.lower().endswith(('png', 'jpg', 'jpeg', 'gif'))]

        if images:  # 如果当前目录有图片，返回图片
            image_path = os.path.join(category_path, random.choice(images))
            return send_file(image_path, mimetype='image/jpeg')

    # 如果两个目录都没有找到图片，则返回 404 页面
    return render_template('404.html'), 404
