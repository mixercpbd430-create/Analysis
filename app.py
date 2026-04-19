"""
Giáo Trình 42 Phương Pháp Phân Tích (Analysis Methods Training)
Flask Web Application
"""
import os
from functools import wraps
from flask import Flask, render_template, abort, jsonify, request, session, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'giaotrinh-analysis-2026')

# --- Authentication ---
ADMIN_USER = os.environ.get('ADMIN_USER', 'Admin')
ADMIN_PASS = os.environ.get('ADMIN_PASS', '2810')


def login_required(f):
    """Decorator kiểm tra đăng nhập"""
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Trang đăng nhập"""
    error = None
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        if username.lower() == ADMIN_USER.lower() and password == ADMIN_PASS:
            session['logged_in'] = True
            session['username'] = username
            next_url = request.args.get('next') or url_for('index')
            return redirect(next_url)
        else:
            error = 'Sai tên đăng nhập hoặc mật khẩu!'
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    """Đăng xuất"""
    session.clear()
    return redirect(url_for('login'))


# Import content
from content import get_all_methods, get_method, get_pillars, get_methods_by_pillar
from content.tpm_dictionary import terms as tpm_terms


@app.route('/')
@login_required
def index():
    """Trang chủ - Tổng quan 42 phương pháp"""
    methods = get_all_methods()
    pillars = get_pillars()
    return render_template('index.html', methods=methods, pillars=pillars)


@app.route('/method/<int:method_id>')
@login_required
def method(method_id):
    """Hiển thị chi tiết phương pháp phân tích"""
    m = get_method(method_id)
    if m is None:
        abort(404)

    methods = get_all_methods()
    prev_m = get_method(method_id - 1)
    next_m = get_method(method_id + 1)

    # Scan method_infographics folder
    infographic_dir = os.path.join(app.static_folder, 'images', 'method_infographics')
    method_infographics = {}  # key -> filename (e.g. 'method_1' -> 'method_1.jpg')
    if os.path.isdir(infographic_dir):
        for fname in os.listdir(infographic_dir):
            name, ext = os.path.splitext(fname)
            if ext.lower() in ('.png', '.jpg', '.jpeg', '.webp'):
                method_infographics[name] = fname

    # Compute global example ID offset for this method
    # Examples are numbered globally: method1 ex1-10, method2 ex11-17, etc.
    from content import ALL_METHODS
    ex_offset = 0
    for am in ALL_METHODS:
        if am['id'] == method_id:
            break
        ex_offset += len(am.get('examples', []))

    return render_template(
        'method.html',
        method=m,
        methods=methods,
        prev_method=prev_m,
        next_method=next_m,
        method_infographics=method_infographics,
        ex_offset=ex_offset
    )


@app.route('/pillar/<pillar_name>')
@login_required
def pillar(pillar_name):
    """Hiển thị các phương pháp theo pillar"""
    methods = get_methods_by_pillar(pillar_name)
    if not methods:
        abort(404)
    all_methods = get_all_methods()
    pillars = get_pillars()
    return render_template('pillar.html',
                           pillar_name=pillar_name,
                           methods=methods,
                           all_methods=all_methods,
                           pillars=pillars)


@app.route('/dictionary')
@login_required
def dictionary():
    """Từ điển TPM - 316 thuật ngữ"""
    # Get unique categories
    categories = sorted(set(t['category'] for t in tpm_terms))
    
    # Scan infographic folder for available images
    infographic_dir = os.path.join(app.static_folder, 'images', 'tpm_infographics')
    infographic_map = {}  # id -> filename
    if os.path.isdir(infographic_dir):
        for fname in os.listdir(infographic_dir):
            name, ext = os.path.splitext(fname)
            if ext.lower() in ('.png', '.jpg', '.jpeg', '.webp'):
                try:
                    infographic_map[int(name)] = fname
                except ValueError:
                    pass
    
    return render_template('dictionary.html',
                           terms=tpm_terms,
                           all_terms=tpm_terms,
                           categories=categories,
                           search_q=request.args.get('q', ''),
                           search_cat=request.args.get('cat', '').strip(),
                           infographic_map=infographic_map)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('index.html',
                           methods=get_all_methods(),
                           pillars=get_pillars(),
                           error="Không tìm thấy trang này"), 404


if __name__ == '__main__':
    print()
    print("  ==========================================")
    print("   GIAO TRINH 42 PHUONG PHAP PHAN TICH")
    print("   Analysis Methods Training Course")
    print("  ==========================================")
    print()
    print("  [URL] http://localhost:5000")
    print()
    app.run(debug=True, host='0.0.0.0', port=5000)
