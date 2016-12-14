from flask import render_template, request, jsonify, current_app
from flask.ext.login import login_required, current_user
from . import main
from ..import db
from ..models import Pic, User


@main.route('/', methods=['GET', 'POST'])
def index():
    page = request.args.get('page', 1, type=int)
    pagination = Pic.query.order_by(Pic.upload_time.desc()).paginate(page,
                    per_page=current_app.config['WEBSITE_PIC_PER_PAGE'],
                    error_out=False)
    pics = pagination.items
    return render_template('index.html', pics=pics, pagination=pagination)


@main.route('/save_img', methods=['POST'])
@login_required
def save_img():
    tag = request.form['tag']
    img_url = request.form['img_url']
    pic = Pic(pic_url=img_url,
              uploader_id=current_user.id,
              tag_name=tag)
    db.session.add(pic)
    db.session.commit()
    return jsonify(tag + ':' + img_url)


@main.route('/user/<name>', methods=['GET', 'POST'])
def user(name):
    user = User.query.filter_by(name=name).first_or_404()
    page = request.args.get('page', 1, type=int)
    pagination = user.pics.order_by(Pic.upload_time.desc()).paginate(page,
                    per_page=current_app.config['WEBSITE_PIC_PER_PAGE'],
                    error_out=False)
    pics = pagination.items
    return render_template('user.html', page=page, user=user,\
                        pagination=pagination,pics=pics)


@main.route('/pic/<id>', methods=['GET', 'POST'])
def pic(id):
    pic = Pic.query.filter_by(id=id).first_or_404()
    return render_template('pic_detail.html', pic=pic)
