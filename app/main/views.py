from flask import render_template, request, jsonify, current_app
from flask.ext.login import login_required, current_user
from . import main
from ..import db
from ..models import Pic


@main.route('/', methods=['GET', 'POST'])
def index():
    pics = Pic.query.all()
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
