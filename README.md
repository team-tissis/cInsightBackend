# CInsight DAO Django Project

```
pipenv install
pipenv shell
python manage.py makemigrations
python manage.py migrate
```

migration がうまくいかない場合は，

```
python manage.py makemigrations api
python manage.py migrate api
```

を試してみると良い．

さらに、postgresql で Database を作って、
settings.py の以下を編集。

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'daofication',
        'USER': 'nishimoto',
        'PASSWORD': '123',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

そして、

```
python manage.py shell_plus
```

起動したら、

```
>>> User(username="hoge").save()
>>> user = User.objects.first()
>>> Token.objects.get_or_create(user=user)
>>> Token.objects.first()
```

これで token が生成されるので、この token をクリップボードにコピーして、
daofication の React のレポジトリの.env.development に、

```
REACT_APP_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

みたいな感じで paste

そして、shell_plus を抜けて、

```
pipenv run server
```

したら、フロントエンドと連携できます。
