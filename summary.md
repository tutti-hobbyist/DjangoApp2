<span style="font-size:120%">

### Djangoの概要・ポイント
#### ファイル構成
- `manage.py` : プロジェクトに関する処理を行うファイル
<br>

- `wsgi.py` : 「web server gateway interface」の略、web serverからの情報をDjangoで受け取れるように情報を加工するプログラムファイル
<br>

- `urls.py` : HTTPリクエストオブジェクトを受け取る処理を行うファイル
    - 第1引数 : URLの指定パス
    - 第2引数 : 第一引数がURLに追記された場合に表示するファイル
    - 第1引数に合致するURLであれば、受け取ったHTTPリクエストオブジェクトを`views.py`に送る
<br>

- `views.py`
    - `urls.py`からHTTPリクエストオブジェクトを受け取り、HTTPレスポンスオブジェクトをwebサーバに返す
<br>

- `setting.py` : 各種設定
    - BASE_DIR : `manage.py`が置いてあるディレクトリのパス
    - SECRET_KEY : パスワードと共に使用される暗号鍵
    - DEBUG : 詳細なログを見たい場合はTrue、本番環境ではFalseにした方が安全
    - ALLOWED_HOST : 情報を受け取るサーバーを指定
    - INSTALLED_APPS : Project内のApplicationのリスト
    - MIDDLEWARE : serverとDjangoの中間処理プログラム
    - ROOT_URLCONF : Djangoがリクエストを受け取ったときに、どのディレクトリの`urls.py`を参照するかを指定
    - TEMPLATES : HTMLテンプレートの情報
    - WSGI_APPLICATION : アプリケーションサーバからの情報取得場所
    - AUTH_PASSWORD_VALIDATORS : パスワード検証
    - STATIC_URL : 様々なファイルを読み込むための設定を行うファイルのURL
<br>

### Tips
- `python manage.py runserver`でローカルサーバを起動し、/adminにアクセスした際にエラーが生じる場合は、`python manage.py migrate`でデータベース中でテーブルを作成し、管理画面機能を有効化する
<br>

- classBasedView vs functionBasedView
    - classBasedView : 手軽に記述できるが拡張性は低い
    - functionBasedView : 1から記述する必要があるが拡張性は高い

</span>