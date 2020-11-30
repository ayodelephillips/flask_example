from flask import render_template, request, Blueprint
from companyBlog.models import BlogPost

core = Blueprint('core', __name__)


@core.route('/')
def index():
    '''
    This is the home page view. Notice how it uses pagination to show a limited
    number of posts by limiting its query size and then calling paginate.
    '''
    page = request.args.get('page', 1, type=int)
    blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page, per_page=10)
    return render_template('index.html',blog_posts=blog_posts)


@core.route('/info')
def info():
    return render_template('info.html')
